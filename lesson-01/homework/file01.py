#!/usr/bin/env python

import sys


def main():
    try:
        import redis
    except ImportError:
        print >> sys.stderr, 'Cannot import "redis", please run ' \
                             'install01.py file to install all necessary ' \
                             'requirements.'
        sys.exit(1)
    else:
        print('All OK!')


if __name__ == '__main__':
    main()
