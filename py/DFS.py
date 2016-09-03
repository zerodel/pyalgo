# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = '''
'''
__author__ = 'zerodel'

LABEL_WHITE = "white"
LABEL_BLACK = "black"
LABEL_GREY = "grey"


def DFS_table(graph):
    # init
    color = dict([(v, LABEL_WHITE) for v in graph])
    parent = dict([(v, "") for v in graph])
    visit_time = dict([(v, -1) for v in graph])
    finish_time = dict([(v, -1) for v in graph])

    time = [0]   # define it as a "global" variable

    def DFS_VISIT(vertex):
        time[0] += 1
        color[vertex] = LABEL_GREY
        visit_time[vertex] = time[0]

        for v in graph[vertex]:
            if color[v] == LABEL_WHITE:
                parent[v] = vertex
                DFS_VISIT(v)

        time[0] += 1
        finish_time[vertex] = time[0]
        color[vertex] = LABEL_BLACK

    for v in graph:
        if color[v] == LABEL_WHITE:
            DFS_VISIT(v)

    return {
        "parent": parent,
        "visit_time": visit_time,
        "finish_time": finish_time
    }


from py.sample_graph import graph22_3
import pprint

dfs_223 = DFS_table(graph22_3)
pprint.pprint(dfs_223)

vs = [v for v in graph22_3]
print(sorted(vs, key = lambda x: dfs_223["finish_time"][x]))




if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass