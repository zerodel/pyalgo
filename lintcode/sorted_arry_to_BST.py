# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''Given a sorted (increasing order) array, Convert it to create a binary tree with minimal height.

 Notice

There may exist multiple valid solutions, return any of them.

Have you met this question in a real interview? Yes
Example
Given [1,2,3,4,5,6,7], return

     4
   /   \
  2     6
 / \    / \
1   3  5   7
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
    @param A: a list of integer
    @return: a tree node
    """

    def sortedArrayToBST(self, A):
        # write your code here
        def split_array(al):
            mid = al[int(round(len(al) / 2))]
            first_part = [x for x in al if x < mid]
            other_part = [x for x in al if x > mid]
            return first_part, [mid], other_part

        def tree_this(al):
            if al:
                lt, this_root, gt = split_array(al)

                if this_root:
                    node = TreeNode(this_root[0])
                    node.left = tree_this(lt)
                    node.right = tree_this(gt)
                    return node
            else:
                return None

        return tree_this(A)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
