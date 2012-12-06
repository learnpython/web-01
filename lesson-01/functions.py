#!/usr/bin/env python

def function():
    return 'Hello, world!'


def function_positional_args(first, *args):
    return ('Hello', first) + tuple(args)


def function_keyword_args(first, second=None, **kwargs):
    return ('Hello', first, second) + tuple(kwargs.items())


def empty():
    pass


def none():
    x = 1
    y = 2
    print 'x + y = ', (x + y)


def exception():
    raise ValueError('Sample exception.')


lambda_function = lambda: 'Hello, world!'
lambda_function_positional_args = lambda first: ', '.join(('Hello', first))


def closure(number):
    def power(to):
        return number ** to
    return power


lambda_closure = lambda number: lambda to: number ** to


def decorator(func):
    def wrapper():
        print('Before function call')
        result = func()
        print('After function call')
        return result
    return wrapper


@decorator
def decorated():
    return 'Hello, world!'


def main():
    print(function)
    print(function())
    print(function_positional_args('world', 'and', 'moon'))
    print(function_keyword_args('world', 'and', third='moon'))
    print(function_keyword_args('world', third='and', fourth='moon'))
    print

    print(empty())
    none()

    try:
        exception()
    except ValueError:
        print('Exception raised.')
        print

    print(lambda_function())
    print(lambda_function_positional_args('world'))
    print

    pow2 = closure(2)
    print pow2(2), pow2(3), pow2(4), pow2(5)

    pow2 = lambda_closure(2)
    print pow2(2), pow2(3), pow2(4), pow2(5)
    print

    print(decorated())


if __name__ == '__main__':
    main()
