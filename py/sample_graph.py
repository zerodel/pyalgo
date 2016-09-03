# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#
__doc__ = '''
'''
__author__ = 'zerodel'

graph22_3 = {
    "v": ["r"],
    "r": ["v", "s"],
    "s": ["r", "w"],
    "w": ["s","t", "x"],
    "t": ["w","x", "u"],
    "x": ["w","t","u","y"],
    "u": ["t", "x", "y"],
    "y": ["x", "u"]
}


grap_v_d = {
    "v1": ["v2", "v4", "v3"],
    "v2": ["v4", "v5"],
    "v3": ["v6"],
    "v4": ["v3", "v6", "v7"],
    "v5": ["v7", "v4"],
    "v6": [],
    "v7": ["v6"]
}

