# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#




__doc__ = '''
'''
__author__ = 'zerodel'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
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

        result =[]
        if root:
            values, level_records = bfs(root)

            d_level = {}
            for value,level in zip(values, level_records):
                d_level.setdefault(str(level), []).append(value)


            for level in sorted([int(level) for level in d_level]):
                raw_level_values = [i for i in d_level[str(level)] if isinstance(i, int)]
                if raw_level_values:
                    result.append(raw_level_values)

        return result


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass