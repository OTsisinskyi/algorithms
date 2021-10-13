import unittest
from discount import discount_search


class TestDiscount(unittest.TestCase):

    def test_discount_search(self):
        products = [1, 1, 1, 50, 50, 1, 50]
        expected = (104.0, 54.0, 50)
        self.assertEqual(discount_search(products), expected)

    def test_discount_search_2(self):
        products = [1, 1, 1, 1, 1, 1, 50, 50, 100, 50]
        expected = (206.0, 106.0, 50)
        self.assertEqual(discount_search(products), expected)

