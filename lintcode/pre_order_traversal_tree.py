# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''
'''
__author__ = 'zerodel'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []

        stack_nodes = []
        now = root
        path = []

        while True:
            while now:
                stack_nodes.append(now)
                path.append(now.val)
                now = now.left

            if stack_nodes:
                now = stack_nodes.pop()
                now = now.right

            else:
                break
        return path

root = TreeNode(1)

root.left = None
p2 = TreeNode(2)
p2.left = TreeNode(3)
root.right = p2

a = Solution()
result = a.preorderTraversal(root)
print("----------------")
print(result)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass

