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

#
# class Solution:
#     """
#     @param root: The root of binary tree.
#     @return: Inorder in ArrayList which contains node values.
#     """
#     def inorderTraversal(self, root):
#         # write your code here
#         if not root:
#             return []
#
#         level = [root]
#         result = [root.val]
#         while root and level:
#             ld = [(x.left, x.right) for x in level if x]
#             for x in level:
#                 if x.right:
#                     result.append(x.right.val)
#                 if x.left:
#                     result.append(x.left.val)
#
#             level = [n for t in ld for n in t if n]
#
#         return result


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        def in_this(node):
            result = []

            left_part = in_this(node.left) if node.left else []
            right_part = in_this(node.right) if node.right else []

            result.extend(left_part)
            result.append(node.val)
            result.extend(right_part)
            return result

        return in_this(root) if root else []


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
