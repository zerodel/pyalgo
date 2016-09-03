# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''
'''
__author__ = 'zerodel'


if __name__ == "__main__":
    import sys
    import math
    n, m, a = sys.argv[1:]
    print(math.ceil(n/a) * math.ceil(m/a))