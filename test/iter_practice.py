# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = '''
'''
__author__ = 'zerodel'




it = iter(range(4))


def try1():
    print("start iteration ")
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
    print("end of iteration")

print("your own iterator")


class ListReverse():
    def __init__(self, some_list):
        self.list = some_list

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.list.pop()
        except:
            raise StopIteration

#
# a = ListReverse(list("hello,world"))
# for x in a:
#     print(x)


a = ["foo", 2, "bar", 4, "far", 6]
group_adjacent = lambda x, k: zip(*([iter(x)] * k))


