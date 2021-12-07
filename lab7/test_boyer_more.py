import unittest
from boyer_moore import *


class TestWChain(unittest.TestCase):

    def test_boyer_moore_1(self):
        text = "Hello, the session is nears"
        pattern = "i"
        self.assertEqual(boyer_moore(text, pattern), [15, 19])

    def test_boyer_moore_2(self):
        text = "Hello, the session is nears"
        pattern = ""
        self.assertEqual(boyer_moore(text, pattern), [None])

    def test_boyer_moore_3(self):
        text = "Hello, the session is nears"
        pattern = "f"
        self.assertEqual(boyer_moore(text, pattern), [None])

    def test_boyer_moore_4(self):
        text = "Hello, the session is nears"
        pattern = " "
        self.assertEqual(boyer_moore(text, pattern), [6, 10, 18, 21])
