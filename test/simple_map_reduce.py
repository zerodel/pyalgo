# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#


import multiprocessing

__doc__ = '''
'''
__author__ = 'zerodel'


class SimpleMapReduce(object):
    def __init__(self, map_func, reduce_func, num_cores=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_cores)

    def __call__(self, inputs, chunk_size=1):
        map_response = self.pool.map(self.map_func, inputs)
        reduce_values = self.pool.map(self.reduce_func,
                                      map_response)
        return reduce_values


def make_random(x):
    return len(x)


def combine(strs):
    return strs


a = SimpleMapReduce(make_random, combine, 4)
a_out = a(["xxx", "yyyyyy", "xxx"])
print(a_out)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
