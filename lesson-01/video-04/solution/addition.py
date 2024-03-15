#!/usr/bin/python

def add(a, b):
    return a + b


def main():
    a = 10
    b = 20
    print('The sum of {} and {} is {}'.format(a, b, add(a, b)))


if __name__ == '__main__':
    main()
