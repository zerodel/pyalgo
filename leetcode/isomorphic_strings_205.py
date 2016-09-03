# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.



__doc__ = '''
'''
__author__ = 'zerodel'


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t = {}
        t2s = {}

        for c1,c2 in zip(s, t):
            if c1 in s2t:
                if not c2 == s2t[c1]:
                    return False
            if c2 in t2s:
                if not c1 == t2s[c2]:
                    return False

            if c1 not in s2t and c2 not in t2s:
                s2t[c1] = c2
                t2s[c2] = c1
        else:
            return True





a = Solution().isIsomorphic

print(a("egg", "add"))
print(a("foo", "bar"))
print(a("paper", "title"))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass