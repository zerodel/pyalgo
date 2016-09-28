# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

"""Given a binary tree, return all root-to-leaf paths.

Have you met this question in a real interview? Yes
Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
]
"""

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
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        def path(node):
            if not node:
                return []
            if not (node.left) and not (node.right):
                return [str(node.val)]
            else:
                pl = path(node.left) if node.left else []
                pr = path(node.right) if node.right else []

                result = []
                result.extend(pl)
                result.extend(pr)
                result = ["->".join([str(node.val), p]) for p in result if p]
                return result

        return path(root)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
