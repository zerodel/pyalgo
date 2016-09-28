# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''
'''
__author__ = 'zerodel'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def bfs(root):
            from collections import deque
            nodes = deque()
            levels = deque()
            values = []
            level_record = []

            nodes.append(root)
            values.append(root.val)
            level_record.append(0)
            levels.append(0)
            while (nodes):
                node_current = nodes.popleft()
                level_current = levels.popleft()
                if node_current.left:
                    nodes.append(node_current.left)
                    values.append(node_current.left.val)
                    levels.append(level_current + 1)
                    level_record.append(level_current + 1)

                else:
                    values.append(None)
                    level_record.append(level_current + 1)

                if node_current.right:
                    nodes.append(node_current.right)
                    values.append(node_current.right.val)
                    levels.append(level_current + 1)
                    level_record.append(level_current + 1)
                else:
                    values.append(None)
                    level_record.append(level_current + 1)

            return values, level_record

        def check_level(values_level):

            for i in range(int(round(len(values_level) / 2))):
                if not values_level[i] == values_level[-1 - i]:
                    return False
            else:
                return True

        if root:
            values, levels = bfs(root)

            d_level = {}
            for value, level in zip(values, levels):
                d_level.setdefault(str(level), []).append(value)

            for level in d_level:
                if not check_level(d_level[level]):
                    return False
            else:
                return True

        else:
            return True


# print(is_tree_symmetric([1,2,2,3,4,4,3]))

# print(is_tree_symmetric([1,2,2,None,3,None,3]))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
