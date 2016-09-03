# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

from linked_list_op_leetcode import *

__doc__ = '''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
__author__ = 'zerodel'



def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head and head.next:
        res = head.next
        dummy = ListNode(0)
        dummy.next = head.next
        pre, now = head.next, head
        while pre and now:
            dummy.next = pre
            now.next, pre.next = pre.next, now            
            dummy, now = now, now.next
            if now:
                pre = now.next
            else:
                break            
        return res
    else:
        return head

llst = val2linklist([1,2,3,4,5,6,7,8,9,0])

print(linklist2vals(swapPairs(llst)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print('---------------------------')
        print(__doc__)
    else:
        pass