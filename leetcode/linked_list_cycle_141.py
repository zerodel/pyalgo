# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = ''' Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

'''
__author__ = 'zerodel'


# a dirty solution
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    path = set()
    while head:
        path.add(head)
        if head.next in path:
            return True
        head = head.next
    return False


# use two pointers , if two pointer has different moving speed , they will eventually meet each other.
def hasCycle2(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow, fast = head, head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
