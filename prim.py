from collections import defaultdict
from unittest import TestCase
import heapq
import unittest

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = defaultdict(list)

    def add_edge(self, src, dest, weight):
        self.edges[src].append((dest, weight))
        self.edges[dest].append((src, weight))

    def prims_mst(self):
        visited = [False] * self.num_vertices
        parent = [-1] * self.num_vertices
        min_heap = [(0, 0, -1)]

        while min_heap:
            weight, vertex, p = heapq.heappop(min_heap)

            if not visited[vertex]:
                visited[vertex] = True
                parent[vertex] = p

                for dest, edge_weight in self.edges[vertex]:
                    if not visited[dest]:
                        heapq.heappush(min_heap, (edge_weight, dest, vertex))

        return parent

# Test cases
class TestPrimsAlgorithm(TestCase):
    def test_prim_small_graph(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 2)
        graph.add_edge(1, 2, 3)
        graph.add_edge(1, 3, 4)
        graph.add_edge(2, 3, 5)

        expected_parent = [-1, 0, 0, 1]
        self.assertEqual(graph.prims_mst(), expected_parent)

    def test_prim_large_graph(self):
        graph = Graph(7)
        graph.add_edge(0, 1, 4)
        graph.add_edge(0, 2, 3)
        graph.add_edge(1, 3, 2)
        graph.add_edge(1, 4, 5)
        graph.add_edge(2, 4, 1)
        graph.add_edge(3, 5, 6)
        graph.add_edge(4, 5, 2)
        graph.add_edge(4, 6, 4)

        expected_parent = [-1, 0, 0, 1, 2, 4, 4]
        self.assertEqual(graph.prims_mst(), expected_parent)

if __name__ == '__main__':
    unittest.main()
