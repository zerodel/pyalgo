from unittest import TestCase

import py.topo_sort
import py.sample_graph

class TestTopo_sort_naive_way_graph_table(TestCase):
    def test_topo_sort_naive_way_graph_table(self):
        print(py.topo_sort.topo_sort_naive_way_graph_table(py.sample_graph.grap_v_d))