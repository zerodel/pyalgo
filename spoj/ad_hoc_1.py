# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#
import sys


__doc__ = ''' rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
'''
__author__ = 'zerodel'

def read_until_42(str_in):
    for i in str_in.strip().split():
        if i.strip() != "42":
            print(i)
        else:
            break


if __name__ == "__main__":
    read_until_42(sys.stdin.read())