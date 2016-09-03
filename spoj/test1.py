# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
# 

import sys

__doc__ = ''' 

Given two natural numbers (both not greater than 200), each number in the separate line, please print the sum of them.
Example

Input:
2
3

Output:
5


'''
__author__ = 'zerodel'


def main():
    a, b = sys.stdin.read().strip().split("\n")
    return int(a.strip()) + int(b.strip())


if __name__ == "__main__":
    print(main())