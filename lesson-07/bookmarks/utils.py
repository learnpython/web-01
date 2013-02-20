from random import choice
from string import digits, letters

from .settings import UID_MAX_LENGTH


def generate_uid(size=None):
    """
    Generate unique ID for bookmark.
    """
    size = size or UID_MAX_LENGTH
    return u''.join([choice(digits + letters) for _ in xrange(size)])
