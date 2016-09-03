# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = '''The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''
__author__ = 'zerodel'

def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    def count_nums(nums):
        pre = nums[0]
        count = 0
        res = []
        for n in nums:
            if n == pre:
                count += 1
            else:
                res.append(str(count))
                res.append(pre)
                pre = n
                count = 1

        res.append(str(count))
        res.append(pre)
        return "".join(res)

    count = 1
    res = "1"
    while count < n:
        res = count_nums(res)
        count +=1
    return res

print(countAndSay(2))

if __name__ == "__main__":
    pass