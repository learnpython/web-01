#!/usr/bin/env python

import os
import sys
import traceback

from os import path
from os.path import abspath

try:
    import does_not_exist
except ImportError:
    if '--traceback' in sys.argv:
        traceback.print_exc()

try:
    from broken import BrokenError
except NameError:
    if '--traceback' in sys.argv:
        traceback.print_exc()


def main():
    print 'Arguments:', sys.argv[1:]
    print 'Basename:', path.basename(__file__)
    print 'Absolute path:', abspath(path.basename(__file__))
    print 'User path:', expanduser('~')


if __name__ == '__main__':
    from os.path import expanduser
    main()
