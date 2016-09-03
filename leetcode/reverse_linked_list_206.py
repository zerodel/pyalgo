# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

from linked_list_op_leetcode import *

__doc__ = ''' Reverse a singly linked list.

click to show more hints.
Hint:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''
__author__ = 'zerodel'


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    n, p = head, head.next

    while p:
        ns = p.next
        p.next = n
        n, p = p, ns
    head.next = None
    return n

ll = val2linklist(list("1234567890"))

print(linklist2vals(reverseList(ll)))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass