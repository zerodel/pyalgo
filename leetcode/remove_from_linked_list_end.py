# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

from linked_list_op_leetcode import *

__doc__ = ''' Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

__author__ = 'zerodel'


# ===============================================================================
# def removeNthFromEnd(head, n):
#     """
#     :type head: ListNode
#     :type n: int
#     :rtype: ListNode
#     """
#     if not head:
#         return None
#     if n == 1:
#         pre, now = None, head
#         while now.next:
#             pre, now = now, now.next
#         if pre:
#             pre.next = None
#         else:
#             return None
#         return head
#
#     from collections import deque
#     pipe =  deque([None] * n)
#     node_this = head
#     while node_this:
#         pipe.append(node_this)
#         pipe.popleft()
#         node_this = node_this.next
#
#     node_this = pipe.popleft()
#     if node_this.next:
#         node_this.val = node_this.next.val
#         node_this.next = node_this.next.next
#     else:
#         return None
#     return head
# ===============================================================================

def removeNthFromEnd(head, n):
    nova_head = ListNode(-1)
    nova_head.next = head
    now, pre = nova_head, nova_head
    for i in range(n):
        pre = pre.next

    while pre.next:
        now, pre = now.next, pre.next

    now.next = now.next.next

    return head


ll = val2linklist([2, 3])
print(linklist2vals(removeNthFromEnd(ll, 1)))

if __name__ == "__main__":
    pass
