#!/usr/bin/env python

def main():
    try:
        open('does_not_exist.exe').read()
    except IOError:
        print('File does_not_exist.exe does not exist.')
    except OSError:
        print('Cannot read from does_not_exist.exe.')
    else:
        print('File does_not_exist.exe exists.')
    finally:
        print('Good bye!')


if __name__ == '__main__':
    main()
