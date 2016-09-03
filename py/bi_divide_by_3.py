#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#


'''
Created on Sep 3, 2016

@author: zerodel
'''




__doc__ = '''
'''
__author__ = 'zerodel'

def long_binary_remainder(str_bin):
    remain_add = {1:2,
                  2:1}
    res_map = dict([((x, y + 1), ( x + y )%3)
                for x in range(3)
                    for y in range(2)])

    remain = 0
    addition = 2
    for n in reversed(str_bin):
        addition = remain_add[addition]
        remain = res_map[(remain, addition)] if n == "1" else remain
    return remain


test_binary_num = "111111110010101010101110101111"

num10 = int(test_binary_num, base=2)

print(num10)
print(num10%3)
print(long_binary_remainder(test_binary_num))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass