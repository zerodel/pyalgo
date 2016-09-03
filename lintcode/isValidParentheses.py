# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Have you met this question in a real interview? Yes
Example
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
__author__ = 'zerodel'

class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        sk = []
        dd = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            if c in "({[":
                sk.append(c)
            if c in dd :
                if sk and dd[c] == sk[-1]:
                    sk.pop()
                else:
                    return False
        return not sk


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass