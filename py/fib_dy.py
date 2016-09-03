# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#
import functools



__doc__ = '''
'''
__author__ = 'zerodel'

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)



from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

fib = memo(fib)




print(fib(9))


if __name__ == "__main__":
    pass