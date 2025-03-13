# flask-microblog

This repository contains my progress on Miguel Grinberg's 2024 version of the
[Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
The tutorial's GitHub repository was
<https://github.com/miguelgrinberg/microblog>. I am typing in the code to
internalize it.

## Getting Started

At the start of this project, I used [Homebrew](https://brew.sh)'s Python 3.13.2 for macOS 15.3.2.
I created a virtual environment, upgraded `pip`, and installed `flask` and its
dependencies.

```console
$ cd ~/src/conradhalling/flask-microblog
$ python3.13 -m venv venv313
$ source venv313/bin/activate
$ pip install --upgrade pip
[output omitted]
Successfully installed pip-25.0.1
$ pip install flask
[output omitted]
Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.2 Werkzeug-3.1.3
 blinker-1.9.0 click-8.1.8 flask-3.1.0 itsdangerous-2.2.0
```

I used the following command to start the application using the Flask
development server on port 5001. I opened the web page at
http://127.0.0.1:5001/.

```console
$ flask --app microblog run --port=5001
 * Serving Flask app 'microblog.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

I used the following command to start the application using the Flask
development server on port 5001 and to allow other devices on my local
network to connect to the app. For example, using my iPad, I could open
the web page at http://arcturus.local:5001/ (where my iPad had IP address
`192.168.0.164` on my local network).

```console
$ flask --app microblog run --host=0.0.0.0 --port=5001
 * Serving Flask app 'microblog.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
* Serving Flask app 'microblog'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://192.168.0.168:5001
Press CTRL+C to quit
192.168.0.164 - - [13/Mar/2025 10:28:05] "GET / HTTP/1.1" 200 -
```

I used the following command to run the Flask development server in debug mode:

```console
$ flask --app microblog run --port 5001 --debug
 * Serving Flask app 'microblog'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 143-135-898
```

I created the following CGI script to run the application in CGI mode. I needed
to test this because the shared hosting servers I used did not support WSGI
applications but did support CGI applications. If I wanted to build a Flask
application and install it in one of my shared hosting accounts. I would be
required to run the application as a CGI application. This worked correctly.

```python
#!/Users/halto/src/conradhalling/flask-microblog/venv313/bin/python3

"""
This CGI script runs the Flask-based microblog application.
"""

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)
```
