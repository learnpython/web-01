#!/usr/bin/env python
# -*- coding: utf-8 -*-

def iterate(data):
    i = 0
    result = []

    for item in data:
        result.append(u'{}. {}'.format(i, item))
        i += 1

    return u'; '.join(result)


def iterate_enumerate(data):
    result = []

    for i, item in enumerate(data):
        result.append(u'{}. {}'.format(i, item))

    return u'; '.join(result)


def main():
    # Boolean type
    # http://docs.python.org/2/library/stdtypes.html#boolean-operations-and-or-not
    xb = True
    yb = False

    if xb:
        print('x is True')

    if not yb:
        print('y is False')

    if xb and not yb:
        print('x is True and y is False')

    if xb or yb:
        print('x is True or y is True')

    if not xb or not yb:
        print('x is False or y is False')

    print

    # Numeric types
    # http://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex
    xi = 2
    yi = 2

    print 'x + y = ', (xi + yi), ', x - y = ', (xi - yi)
    print 'x * y = ', (xi * yi), ', x / y = ', (xi / yi)

    yf = 2.0

    print 'x + y = ', (xi + yf), ', x - y = ', (xi - yf)
    print 'x * y = ', (xi * yf), ', x / y = ', (xi / yf)
    print

    # Sequence types
    # http://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange
    xl = [1, 2, 3]
    xs = 'String'
    xt = (1, 2, 3)
    xu = u'Строка'

    print 'String:', xs, len(xs), 's' in xs, 'S' in xs
    print 'Unicode:', xu, len(xu), u'с' in xu, u'С' in xu
    print 'List:', xl, len(xl), 1 in xl, xl.index(1)
    print 'Tuple:', xt, len(xt), 1 in xt, xt.index(1)

    print iterate(xs), '         ', iterate_enumerate(xs)
    print iterate(xu), '         ', iterate_enumerate(xu)
    print iterate(xl), '         ', iterate_enumerate(xl)
    print iterate(xt), '         ', iterate_enumerate(xt)

    xl.append(4)

    try:
        xt.append(4)
    except AttributeError:
        print('Cannot add value to tuple. Tuple is immutable!')
        print

    # Set types
    # http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
    xf = frozenset([1, 2, 3, 4, 5, 1, 2, 3, 6])
    xs = {1, 2, 3, 4, 5, 1, 2, 3, 6}

    print 'Set:', xs, 1 in xs, xs.union({2, 7}), xs & {1, 2}, xs - {1, 2}
    print 'Frozenset:', xf, 1 in xf, xf.union({2, 7}), xf & {1, 2}, xf - {1, 2}

    xs.add(7)

    try:
        xf.add(7)
    except AttributeError:
        print('Cannot add value to frozenset. Frozenset is immutable!')
        print

    # Mapping type
    # http://docs.python.org/2/library/stdtypes.html#mapping-types-dict
    xd = {1: 'a', 2: 'b', 3: 'c'}

    print 'Dict:', xd, len(xd), 1 in xd, 'a' in xd
    print xd.keys(), xd.values(), xd.items()

    xd[4] = 'd'
    xd.update({5: 'e'})
    xd.setdefault(6, 'f')

    print 'Updated dict:', xd
    print

    # File objects
    # http://docs.python.org/2/library/stdtypes.html#file-objects
    handler = open(__file__)
    content = handler.read()

    print 'File:', handler
    print 'Content length:', len(content)

    content = handler.read()
    handler.close()

    print 'Closed file:', handler
    print 'Empty content:', content, len(content)


if __name__ == '__main__':
    main()
