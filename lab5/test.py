import unittest
from main import *


class TestMain(unittest.TestCase):

    def test_ford_fulkerson(self):
        graph = [[0, 10, 5, 0],
                 [0, 0, 0, 20],
                 [0, 0, 0, 5],
                 [0, 0, 0, 0]]
        g = Graph(graph, source=0, sink=3)

        expected = 15
        self.assertEqual(g.ford_fulkerson(), expected)
