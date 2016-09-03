# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

import math

from py.sample_graph import graph22_3

__doc__ = '''
'''
__author__ = 'zerodel'

label_v = {
    "b": "black",
    "w": "white",
    "g": "grey"}


def BFS_table(table_graph, start):
    # init
    color = dict([(v, label_v["w"]) for v in table_graph])
    parent = dict([(v, "") for v in table_graph])
    depth  = dict([(v, math.inf) for v in table_graph])

    working_fifo = []

    # start
    working_fifo.append(start)
    depth[start] = 0

    while(working_fifo):
        v_now = working_fifo.pop(0)

        for v in table_graph[v_now]:
            if color[v] == label_v["w"]:
                color[v] = label_v["g"]
                parent[v] = v_now
                depth[v] = depth[v_now] + 1

                working_fifo.append(v)

        color[v_now] = label_v["b"]

    return {"color": color,
            "parent": parent,
            "depth": depth,
            "neighbour_table": table_graph
            }


def extract_path_from_bfs(bfs_result, end):
    p = end
    tree_backward = bfs_result["parent"]
    path = []
    while tree_backward[p]:
        path.append(p)
        p = tree_backward[p]
    path.append(p)
    return [p for p in reversed(path)]


def bfs_shortest_path(table_graph, start, end,bfs_result=None):
    if not bfs_result:
        bfs_result = BFS_table(table_graph, start)
    return extract_path_from_bfs(bfs_result, end)


print(bfs_shortest_path(graph22_3, "s", "y"))



if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass