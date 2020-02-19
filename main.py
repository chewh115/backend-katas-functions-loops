#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = """chewh115, and Rob, David and I talked about how to handle
negatives, so I incorporated that in my code as well."""


def add(x, y):
    """Add two integers. Handles negative values."""
    return x+y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    negative = False
    if x < 0 and y > 0:
        negative = True
    elif x > 0 and y < 0:
        negative = True
    x = abs(x)
    y = abs(y)
    total = 0
    for _ in range(y):
        total = add(total, x)
    if negative:
        total = -total
    return total


def power(x, n):
    """Raise x to power n, where n >= 0"""
    total = 1
    for _ in range(n):
        total = multiply(total, x)
    return total


def factorial(x):
    """Compute factorial of x, where x > 0"""
    total = 1
    for i in range(x):
        total = multiply(total, (x-i))
    return total


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    total = 0
    prev_num = 0
    prev_prev_num = 1
    for i in range(n):
        total = add(prev_prev_num, prev_num)
        prev_prev_num = prev_num
        prev_num = total
    return total


if __name__ == '__main__':
    # your code to call functions above
    pass
