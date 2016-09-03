# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''
'''
__author__ = 'zerodel'

def hh(line):
    return ''.join([n for i,n in enumerate(line[:len(line)/2]) if i%2 == 0])

import sys
inputs = sys.stdin.read().strip().split("\n")
num = int(inputs[0].strip())
res = "\n".join([hh(line.strip())for line in inputs[1:num + 1]])
print(res)