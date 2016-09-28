# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = '''  Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
__author__ = 'zerodel'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        lp, lq = [p], [q]

        while any(lp) or any(lq):
            vp = [x.val if x else None for x in lp]
            vq = [x.val if x else None for x in lq]

            for x in zip(vp, vq):
                if not x[0] == x[1]:
                    return False

            nlp = [(x.left, x.right) for x in lp if x]
            nlq = [(x.left, x.right) for x in lq if x]

            lp = [n for t in nlp for n in t]
            lq = [n for t in nlq for n in t]
        return True

a = [None, None, None]




