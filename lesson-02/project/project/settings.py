"""
================
project.settings
================

Place project settings here.

"""

import os


# Dummy project settings
DUMMY = True
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Overwrite current username
USER = 'dummy'


# Load more settings from local
try:
    from project import settings_local
except ImportError:
    pass
else:
    for attr in dir(settings_local):
        if attr.startswith('_'):
            continue
        locals()[attr] = getattr(settings_local, attr)
