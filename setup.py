from setuptools import setup, find_packages

def main():
    setup(
        name='csp_eventlet_jsio_example',
        version=1,
        author='Michael Carter',
        author_email='CarterMichael@gmail.com',
        long_description='',
        packages= find_packages(),
        zip_safe = False,
        install_requires = ['csp_eventlet', 'eventlet', 'paste'],
        entry_points = '''    
            [console_scripts]
            csp_eventlet_jsio_example = csp_eventlet_jsio_example.start:main
        ''',
        
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],        
    )


if __name__ == '__main__':
    main()
