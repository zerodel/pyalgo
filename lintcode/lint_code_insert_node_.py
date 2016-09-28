# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''
'''
__author__ = 'zerodel'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        level = [root]
        while root and level:
            ld = []
            for x in level:
                if (not x.left) == (not x.right):
                    ld.append((x.left, x.right))
                else:
                    if x.left:
                        x.right = node
                    else:
                        x.left = node
                    return
            level = [n for t in ld for n in t]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
