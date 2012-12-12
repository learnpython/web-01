"""
============
project.main
============

Web-page which shows current environment as JSON.

"""

from project.utils import get_environ_json


def app(environ, start_response):
    """
    Displays current environment as JSON.
    """
    data = get_environ_json(indent=4)
    start_response('200 OK', [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(data))),
    ])
    return iter([data])
