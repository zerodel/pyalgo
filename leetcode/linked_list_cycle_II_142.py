# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''
__author__ = 'zerodel'


def detectCycle1(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    path = set()
    while head:
        if head in path:
            return head
        else:
            path.add(head)

        head = head.next

    return None


def detectCycle2(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow, fast = head, head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    while head != fast:
        head = head.next
        fast = fast.next
    return head


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
