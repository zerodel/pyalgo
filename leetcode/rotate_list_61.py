# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

from linked_list_op_leetcode import *

__doc__ = ''' Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
__author__ = 'zerodel'


def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head is None or k == 0:
        return head
    h_bak, end, h_new = head, head, head

    counter = 0
    lst = 0
    hl = head
    while hl:
        hl = hl.next
        lst += 1

    k = k % lst
    if k == 0:
        return head
    while head.next:
        head = head.next
        counter += 1
        if counter == k - 1:
            end = head
        if counter == k:
            h_new = head

    if h_new:
        head.next = h_bak
        end.next = None
        head = h_new
    return head


# def rotateRight(head, k):
#     """
#     :type head: ListNode
#     :type k: int
#     :rtype: ListNode
#     """
#     if head is None or k == 0:
#         return head
#
#
#     from collections import deque
#     nodes = deque([])
#     while head:
#         nodes.append(head)
#         head = head.next
#
#     for x in range(k%len(nodes)):
#         nodes.appendleft(nodes.pop())
#
#     for i in range(len(nodes) -1):
#         nodes[i].next = nodes[i+1]
#     nodes[-1].next = None
#
#     return nodes[0]

# [1,2,3]
# 2000000000

ll = val2linklist(list("123"))

print(linklist2vals(rotateRight(ll, 2000000000)))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
