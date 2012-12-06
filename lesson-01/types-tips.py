#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import timeit


def append(item, data=[]):
    data.append(item)
    return data


def fix_append(item, data=None):
    data = data or []
    data.append(item)
    return data


def main():
    # Swapping values
    x, y = 1, 2
    x, y = y, x
    print 'x:', x, ', y:', y
    print

    # Numeric types tips
    x = 5
    y = 3

    print 'x // y = ', x // y, ', x % y = ', x % y, ', x ** y = ', x ** y

    try:
        x / 0
    except ZeroDivisionError:
        print('Cannot divide to zero.')
        print

    # Sequence types tips
    try:
        'к' in u'Строка'
    except UnicodeDecodeError:
        print('Cannot find non-ascii string in unicode.')

    append(1)
    append(2)
    x = append(3)

    fix_append(1)
    fix_append(2)
    y = fix_append(3)

    print 'x:', x, ', y:', y
    print

    x = []
    y = x
    x.append(1)
    print 'x:', x, ', y:', y
    print 'id(x):', id(x), ', id(y):', id(y)

    x = []
    y = copy.copy(x)
    x.append(1)
    print 'x:', x, ', y:', y
    print 'id(x):', id(x), ', id(y):', id(y)

    x = [[]] * 6
    print 'x:', x

    y = x
    y[0].append(1)
    print 'y:', y, ', x:', x

    x = [[]] * 6
    y = copy.copy(x)
    y[0].append(1)
    print 'y:', y, ', x:', x

    x = [[]] * 6
    y = copy.deepcopy(x)
    y[0].append(1)
    print 'y:', y, ', x:', x
    print

    # Indexes, slices, reverses, sort
    x = [1, 2, 3, 4, 5, 6, 9, 8, 7]
    print '[:3]', x[:3], ', [3:]', x[3:], ', [4:6]', x[4:6]
    print '[-1]', x[-1], ', [-2:]', x[-2:], ', [:-2]', x[:-2]
    print 'reverse:', x[::-1], 'reversed:', list(reversed(x))
    print 'sort:', sorted(x), 'reversed:', sorted(x, reverse=True)
    print

    # Search in sets faster than search in sequences
    number = 1000000

    xt = timeit.timeit('100 in x', 'x = range({})'.format(number), number=1000)
    yt = timeit.timeit('100 in x',
                       'x = list(range({}))'.format(number),
                       number=1000)
    zt = timeit.timeit('100 in x',
                       'x = set(range({}))'.format(number),
                       number=1000)

    print 'List:', xt * 1000, ', tuple:', yt * 1000, ', set:', zt * 1000
    print

    # Mapping types tips
    x = {'a': 1, 'b': 2, 'c': 3}
    y = x
    x['d'] = {}
    print 'x:', x, ', y:', y
    print 'id(x):', id(x), ', id(y):', id(y)

    x = {}
    x['a'] = 1
    x['b'] = 2
    x.update({'c': 3, 'd': 4, 'e': 5})
    x['f'] = 6
    print 'x:', x
    print

    # File objects context manager
    with open(__file__) as handler:
        content, empty = handler.read(), handler.read()

        print 'File:', handler
        print 'Content:', len(content)
        print 'Empty:', len(empty)


if __name__ == '__main__':
    main()
