# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8


'''
__author__ = 'zerodel'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 and not l2:
        return None

    res_num, a, b, c, add = [], 0, 0, 0, 0
    while l1 or l2:

        if l1 and l2:
            a, b = l1.val , l2.val
            l1 , l2 = l1.next, l2.next
            c = a + b + add
        else:
            if l1:
                c = l1.val + add
                l1 = l1.next
            if l2:
                c = l2.val + add
                l2 = l2.next

        add = 0
        if c >= 10:
            c = c - 10
            add = 1
        res_num.append(c)

    if add == 1:
        res_num.append(add)

    res_nodes = [ListNode(x) for x in res_num]
    for i in range(len(res_num) - 1):
        res_nodes[i].next = res_nodes[i+1]

    return res_nodes[0]
#    return res_num

a1 = ListNode(2)
b1 = ListNode(4)
c1 = ListNode(3)
a1.next = b1
b1.next = c1

a2 = ListNode(5)
b2 = ListNode(6)
c2 = ListNode(4)
a2.next = b2
b2.next = c2

print(addTwoNumbers(a1, a2))

if __name__ == "__main__":
    pass