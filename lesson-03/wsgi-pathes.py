#!/usr/bin/env python

from wsgiref.simple_server import make_server


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    path = environ['PATH_INFO']

    if path == '/':
        yield 'Hello, world!'
    elif path == '/moon':
        yield 'Hello, moon!'
    else:
        yield 'Page not found'


if __name__ == '__main__':
    server = make_server('0.0.0.0', 8001, app)

    try:
        print('Running on http://0.0.0.0:8001/')
        server.serve_forever()
    except KeyboardInterrupt:
        print
