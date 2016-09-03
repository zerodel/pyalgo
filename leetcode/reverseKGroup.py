# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#
from linked_list_op_leetcode import *


__doc__ = ''' Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
__author__ = 'zerodel'

def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if k < 2:
        return head

    if head is None or head.next is None:
        return head

    pre = ListNode(-1)
    pre.next = head

    dum_backup = pre

    while True:
        sentry_k = pre
        for x in range(k):
            if sentry_k.next:
                sentry_k = sentry_k.next
            else:
                return dum_backup.next

        n, b = pre.next, pre.next.next
        for x in range(k - 1):
            step_forward = b.next
            b.next = n
            n, b = b, step_forward

        next_pre = pre.next
        next_pre.next = step_forward
        pre.next = n
        pre = next_pre


ll = val2linklist(list("1234567890"))

print(linklist2vals(reverseKGroup(ll, 4)))


if __name__ == "__main__":
    pass