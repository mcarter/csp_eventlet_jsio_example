import os
import eventlet.wsgi

from paste import urlmap, urlparser
from csp_eventlet import Listener

static_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'static')

class Server(object):
  
    def __init__(self, interface='', port=8000):
        self.wsgi = urlmap.URLMap()
        self.wsgi['/'] = urlparser.StaticURLParser(static_path)
        self.csp_listener = Listener()
        self.wsgi['/csp'] = self.csp_listener
        self.interface = interface
        self.port = port
        
    def run(self):
        eventlet.spawn(eventlet.wsgi.server, eventlet.listen((self.interface, self.port)), self.wsgi)
        while True:
            sock, addr = self.csp_listener.accept()
            eventlet.spawn(self.dispatch, sock, addr)
            
    def dispatch(self, sock, addr):
        sock.send('Welcome!')
        while True:
            try:
                print 'wait for data'
                data = sock.recv(4096)
                print 'Received', data
                if not data:
                    # socket is closed
                    break
                sock.send(data)
            except Exception, e:
                print 'Exception with csp sock', sock, e
                break
        print 'csp socket is closed'

if __name__ == "__main__":
    s = Server()
    try:
        s.run()
    except KeyboardInterrupt:
        print "Ctr-C pressed, exiting"