# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

'''
__author__ = 'zerodel'


def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    from math import floor
    stk = []
    for x in tokens:
        if x in "+-*/":
            b = stk.pop()
            a = stk.pop()
            if x == "+":
                stk.append(str(int(a) + int(b)))
            if x == "-":
                stk.append(str(int(a) - int(b)))
            if x == "*":
                stk.append(str(int(a) * int(b)))
            if x == "/":
                stk.append(str(floor(int(a) / int(b))))
        else:
            stk.append(x)

    return int(stk[-1])


print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

if __name__ == "__main__":
    pass
