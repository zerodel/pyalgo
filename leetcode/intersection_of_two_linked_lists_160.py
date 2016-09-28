# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

from linked_list_op_leetcode import convert_to_list_of_nodes

__doc__ = '''Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''
__author__ = 'zerodel'


def getIntersectionNode_ugly(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA and headB:
        sa, sb = [], []
        ta, tb = headA, headB
        while ta:
            sa.append(ta)
            ta = ta.next
        while tb:
            sb.append(tb)
            tb = tb.next
        last = None
        while sa and sb and sa[-1] == sb[-1]:
            last = sa.pop()
            last = sb.pop()

        return last
    else:
        return None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    pass


def getIntersectionNode_ugly2(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA and headB:
        # calculate the length
        la, lb, na, nb = 0, 0, headA, headB
        while na:
            la, na = la + 1, na.next
        while nb:
            lb, nb = lb + 1, nb.next

        abs_diff = abs(la - lb)

        for i in range(abs_diff):
            if la > lb:
                headA = headA.next
            else:
                headB = headB.next
        while headA != headB:
            if headA and headB:
                headA, headB = headA.next, headB.next
            else:
                return None
        return headA

    else:
        return None


a = convert_to_list_of_nodes([2, 3])
b = convert_to_list_of_nodes([4, 5, 6, 1])
c = convert_to_list_of_nodes([7, 8, 9])
a[-1].next = c[0]
b[-1].next = c[0]

jointer = getIntersectionNode_ugly2(a[0], b[0])
if jointer:
    print(jointer.val)
else:
    print("Null")

if __name__ == "__main__":
    pass
