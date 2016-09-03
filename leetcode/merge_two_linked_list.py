# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

import sys
import os

from linked_list_op_leetcode import *
__doc__ = '''
'''
__author__ = 'zerodel'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    hd = dummy

    while l1 and l2:
        if l1.val >= l2.val:
            hd.next = l2
            l2 = l2.next
        else:
            hd.next = l1
            l1 = l1.next

        hd = hd.next
    hd.next = l1 if l1 else l2

    return dummy.next


l1 = val2linklist([])
l2 = val2linklist([])

print(linklist2vals(mergeTwoLists(l1, l2)))

if __name__ == "__main__":
    pass