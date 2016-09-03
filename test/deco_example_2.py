# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' ------------------------------
try the decorator with a class as argument
'''
__author__ = 'zerodel'

class t1(object):
    def __init__(self):
        pass

    @staticmethod
    def establish():
        print("t1 established")
    @staticmethod
    def self_destory():
        print("t1 destroyed")

def deco(cls):
    def _func(func):
        def _par(*args, **kwargs):
            print("before invoking : {}".format(func.__name__))
            cls.establish()
            func(cls,*args, **kwargs)
            cls.self_destory()

        return _par
    return _func


@deco(t1)
def go_for_it(x, *args, **kwargs):
    print("finally , we get the context x: {}".format(x))


go_for_it()



if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass