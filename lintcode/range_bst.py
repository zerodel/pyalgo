# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.

Have you met this question in a real interview? Yes
Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
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
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        check = lambda x: x <= k2 and x >= k1
        if not root:
            return []

        if not root.left and not root.right:
            return [root] if check(root.val) else []

        nodes = []
        level = [root]

        while level:
            ld = [(x.left, x.right) for x in level if x]
            nodes.extend(level)
            level = [n for t in ld for n in t if n]

        return [x for x in sorted([n.val for n in nodes if n and check(n.val)])]

    def reur(self, root, k1, k2):
        check = lambda x: x <= k2 and x >= k1
        if not root:
            return []

        if not root.left and not root.right:
            return [root] if check(root.val) else []

        def on_node(node):

            lr = on_node(node.left) if node.left else []
            rr = on_node(node.right) if node.right else []

            result = []
            result.extend(lr)
            if check(node.val):
                result.append(node.val)
            result.extend(rr)

            return result

        return [x for x in sorted(on_node(root))]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
