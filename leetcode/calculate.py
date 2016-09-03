# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = '''Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

Note: Do not use the eval built-in library function.

https://leetcode.com/problems/basic-calculator/
'''
__author__ = 'zerodel'


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return cal_reverse_expression(make_reverse_expression(s))


def split_string(str_raw):
    se = list(str_raw)

    res = []
    rt = []
    while se:
        op = se.pop()
        if op in "+-()":
            if rt:
                rt = [x for x in reversed(rt)]
                res.append(rt)
                rt = []
            res.append([op])
        else:
            if rt:
                rt.append(op)
            else:
                rt = [op]
    rt = [x for x in reversed(rt)]
    res.append(rt)

    uniformed = ["".join(seg).strip() for seg in reversed(res)]
    return [x for x in uniformed if x and not x == " "]

def is_int(x):
    op = "+-()"
    for i in op:
        if i in x:
            return False
    else:
        return True

def cal_reverse_expression(reverse_polish):
    s = []
    for c in reverse_polish:
        if is_int(c):
            s.append(int(c))
        else:
            post = s.pop()
            pre = s.pop()
            if c == "+":
                s.append(pre + post)
            elif c == "-":
                s.append(pre - post)

    return s[-1]

def make_reverse_expression(str_raw):
    op = []
    res = []
    divided = split_string(str_raw)
    for c in divided:
        if is_int(c):
            res.append(c)
        else:
            if c == "(":
                op.append(c)
            elif c in "+-":
                if op and not op[-1] == "(":
                    res.append(op.pop())
                op.append(c)
            elif c == ")":
                while True:
                    in_par = op.pop()
                    if in_par == "(":
                        break
                    res.append(in_par)
    while op:
        res.append(op.pop())
    return res


s = "   (  3 ) "
print(cal_reverse_expression(make_reverse_expression(s)))

if __name__ == "__main__":
    pass