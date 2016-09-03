# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
__author__ = 'zerodel'


def twosum(nums, target):
    dd = {}
    for i,x in enumerate(nums):
        if x in dd:
            return [dd[x], i]
        else:
            dd[target - x] = i


print(twosum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    pass