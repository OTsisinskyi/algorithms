import unittest
from wchain import *


class TestWChain(unittest.TestCase):

    def test_wchain_1(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(max_chain(words), 4)

    def test_wchain_2(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(max_chain(words), 1)
