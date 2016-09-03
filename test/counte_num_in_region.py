# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = '''
'''
__author__ = 'zerodel'


class CounterRegion(object):
    def __init__(self, lst_given):
        from math import inf
        self.lst = [-1]
        self.lst.extend(sorted(lst_given))
        self.lst.append(inf)

        self.s = 0
        self.e = 0

    def count(self, r1, r2):
        if r1 == r2:
            return 0
        rside = r1 if r1 > r2 else r2
        lside = r1 if r1 < r2 else r2

        self._move_start(lside)
        self._move_end(rside)
        return self.e - self.s + 1

    def _move_start(self, lside):
        s = self.s
        s2 = s
        if self.lst[s] < lside:
            while self.lst[s] < lside:
                s, s2 = s + 1, s
            self.s = s
        else:
            while self.lst[s] > lside:
                s, s2 = s - 1, s
            self.s = s2

    def _move_end(self, rside):
        e = self.e
        e2 = e
        if self.lst[e] < rside:
            while self.lst[e] < rside:
                e, e2 = e + 1, e
            self.e = e2
        else:
            while self.lst[e] > rside:
                e, e2 = e - 1, e
            self.e = e

a = [x for x in range(0, 999999, 3)]

b = CounterRegion(a)
print(b.count(9, 9))
print(b.count(9, 9999))

# import timeit
# print(timeit.timeit("b.count(9, 9999)", setup="from __main__ import b"))
if __name__ == "__main__":
    pass