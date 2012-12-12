"""
=============
project.utils
=============

Utilities for test project.

get_environ_json
================

Get current environment, update it with project settings and dumps result to
JSON.

"""

import json
import os

from project import settings


def get_environ_json(**kwargs):
    """
    You should overwrite any keyword argument which passed to ``json.dumps``
    function.
    """
    settings_data = dict([
        (attr, getattr(settings, attr)) for attr in dir(settings) \
        if attr.isupper()
    ])

    data = dict(os.environ)
    data.update(settings_data)

    return json.dumps(data, **kwargs)
