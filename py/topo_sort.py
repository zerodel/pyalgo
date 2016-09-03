# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''
'''
__author__ = 'zerodel'

def find_vertex_zero_in_degree_graph_table(graph_table):
    for key in graph_table:
        if is_zero_input_degree(key, graph_table):
            return key

def is_zero_input_degree(vertex, graph):
    for v in graph:
        if vertex in graph[v]:
            return False
    return True

def topo_sort_naive_way_graph_table(graph_table):
    topo_path = []
    while(graph_table):
        v_root = find_vertex_zero_in_degree_graph_table(graph_table)
        topo_path.append(v_root)
        graph_table.pop(v_root)
    return topo_path

def calculate_in_degree(vertex, graph):
    in_degree = 0
    for v in graph:
        if vertex in graph[v]:
            in_degree += 1
    return in_degree


def topo_sort_improved(graph_table):
    topo_path = []
    in_degree_table = dict([(v, calculate_in_degree(v, graph_table)) for v in graph_table])

    zero_in_degree_v = [v for v in graph_table if in_degree_table[v] == 0]

    while(graph_table):
        pop_v = zero_in_degree_v.pop(0)
        topo_path.append(pop_v)
        for v in graph_table.pop(pop_v):
            in_degree_table[v] -= 1
            if in_degree_table[v] == 0:
                zero_in_degree_v.append(v)

    return topo_path





if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass