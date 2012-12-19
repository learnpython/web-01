#!/usr/bin/env python

from flup.server.fcgi import WSGIServer


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello, world!'


if __name__ == '__main__':
    WSGIServer(app).run()
