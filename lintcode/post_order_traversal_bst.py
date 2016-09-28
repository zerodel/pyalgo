# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' Given a binary tree, return the postorder traversal of its nodes' values.

Have you met this question in a real interview? Yes
Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [3,2,1].
'''
__author__ = 'zerodel'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        path = [root]
        last = None
        visited = []
        while path:
            node = path[-1]
            if (not node.left and not node.right) or ((last is not None) and (last == node.right or last == node.left)):
                last = path.pop()
                visited.append(last.val)
                if not path:
                    break
            else:
                if node.right:
                    path.append(node.right)
                if node.left:
                    path.append(node.left)
        return visited


root = TreeNode(1)

root.left = None
p2 = TreeNode(2)
p2.left = TreeNode(3)
root.right = p2

a = Solution()
print(a.postorderTraversal(root))

if __name__ == "__main__":
    pass
