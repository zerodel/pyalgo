# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
__author__ = 'zerodel'

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dd = {}
        for n in nums:
            if n in dd:
                dd[n] += 1
            else:
                dd[n] = 1
        for n in dd:
            if dd[n] > len(nums)/2:
                return n


    def majorityElement2(self, nums):
        counter, co = 0, 0
        for i in nums:
            if 0 == counter:
                co = i
                counter = 1
            elif i == co:
                counter += 1
            else:
                counter -= 1

        # here , you should validate that co is the answer,
        return co


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
