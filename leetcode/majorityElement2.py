# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
'''
__author__ = 'zerodel'


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def boyer_moore_most_vote(nums):
            n0, n1, c0, c1 = None, None, 0, 0
            for i in nums:
                if i == n0:
                    c0 += 1
                elif i == n1:
                    c1 += 1
                elif c0 == 0:
                    c0 = 1
                    n0 = i
                elif c1 == 0:
                    c1 = 1
                    n1 = i
                else:
                    c1 -= 1
                    c0 -= 1

            c0, c1 = 0, 0
            for i in nums:
                if i == n0:
                    c0 += 1
                elif i == n1:
                    c1 += 1
            result =[]
            if c0 > len(nums)/3:
                result.append(n0)
            if c1 > len(nums)/3:
                result.append(n1)
            return result

        return boyer_moore_most_vote(nums)
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass