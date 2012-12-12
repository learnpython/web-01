import os

from library import to_json


def app(environ, start_response):
    data = to_json(dict(os.environ))
    start_response('200 OK', [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(data))),
    ])
    return iter([data])