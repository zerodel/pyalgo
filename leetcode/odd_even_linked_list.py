# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

from linked_list_op_leetcode import *

__doc__ = ''' Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''
__author__ = 'zerodel'


def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head and head.next:
        o = head
        e = head.next
        he = head.next

        while e.next and o.next:
            o.next = e.next
            o = o.next
            if not o.next:
                break
            e.next = o.next
            e = e.next

        o.next = he
        e.next = None
    return head


a = val2linklist([])
lks = oddEvenList(a)

print(linklist2vals(lks))

if __name__ == "__main__":
    pass
