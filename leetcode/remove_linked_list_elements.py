# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
__author__ = 'zerodel'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_elements(head, val):
    while head and head.val == val:
        head = head.next

    if not head:
        return None

    prev, cur = head, head.next

    while cur:
        while cur and cur.val == val:
            cur = cur.next
        prev.next = cur
        if cur:
            prev, cur = cur, cur.next

    return head


#
# def remove_elements(head, val):
#     values = []
#     while head:
#         values.append(head.val)
#         head = head.next
#
#     filtered_values = [x for x in values if not x == val]
#
#     if filtered_values:
#         nodes = [ListNode(x) for x in filtered_values]
#         for i in range(len(nodes) - 1):
#             nodes[i].next = nodes[i+1]
#         return nodes[0]
#     else:
#         return None
#
#



# the last one

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
