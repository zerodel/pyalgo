# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#


__doc__ = '''
'''
__author__ = 'zerodel'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def convert_to_list_of_nodes(vals):
    if not vals:
        return None

    nodes = [ListNode(val) for val in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes


def val2linklist(vals):
    nodes = convert_to_list_of_nodes(vals)
    if nodes:
        return nodes[0]
    else:
        return None


def linklist2vals(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next

    return vals


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
