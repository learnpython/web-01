#!/usr/bin/env python

import os
import sys

from subprocess import call


DIRNAME = os.path.abspath(os.path.dirname(__file__))
ENV = 'env'
REQUIREMENTS = 'requirements.txt'


def check_env():
    """
    Check if env directory already created, if did not - create new one.
    """
    print('== Step 1. Create virtual environment ==')

    if os.path.isdir(ENV):
        print('Virtual environment {} already created.'.
              format(os.path.basename(ENV)))
    else:
        call('virtualenv --use-distribute {}'.format(ENV), shell=True)


def check_virtualenv():
    """
    Check if virtualenv installed in our system or not.
    """
    try:
        import virtualenv
    except ImportError:
        print >> sys.stderr, 'virtualenv not installed to this system.'
        sys.exit(1)


def install_requirements():
    """
    Install all requirements to virtual environment.
    """
    print('== Step 2. Install requirements ==')
    call('{}/bin/pip install -r {}'.format(ENV, REQUIREMENTS), shell=True)


def main():
    """
    Main function to do all necessary actions.
    """
    # Make sure we work in directory next to current file
    os.chdir(DIRNAME)

    check_virtualenv()
    check_env()
    install_requirements()


if __name__ == '__main__':
    main()
