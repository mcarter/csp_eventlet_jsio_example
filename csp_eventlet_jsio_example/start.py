from server import Server

def main():
    s = Server()
    try:
        s.run()
    except KeyboardInterrupt:
        print "Ctr-C pressed, exiting"
  
  


if __name__ == "__main__":
    main()
