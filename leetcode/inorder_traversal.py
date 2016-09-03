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
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []

        node = root
        path =[]
        stk = []

        while True:
            while node:
                stk.append(node)
                node = node.left

            if stk:
                node = stk.pop()
                path.append(node.val)
                print(node.val)
                node = node.right
            else:
                break
        return path





# test
root = TreeNode(1)

p2 = TreeNode(2)
p2.left = TreeNode(3)
root.right = p2

a = Solution()
result = a.inorderTraversal(root)
print("----------------")
print(result)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass