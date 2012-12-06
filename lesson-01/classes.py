#!/usr/bin/env python


class Rectangle(object):

    a = None
    b = None
    name = 'Rectangle'

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return self.name

    def sqr(self):
        return self.a * self.b


class Square(Rectangle):

    name = 'Square'

    def __init__(self, a):
        self.a, self.b = a, a


def main():
    rect = Rectangle(10, 20)
    print rect, rect.sqr()

    square = Square(20)
    print square, square.sqr()


if __name__ == '__main__':
    main()
