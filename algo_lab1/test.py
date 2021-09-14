from quick_sort import *
import unittest


class TestQuickSort(unittest.TestCase):
    def test_asc(self):
        array = [0, 4, 6, 10, 8, 2]
        quick_sort(array, 0, len(array) - 1, "ASC")
        self.assertEqual(array, sorted(array))

    def test_decs(self):
        array = [0, 4, 6, 10, 8, 2]
        quick_sort(array, 0, len(array) - 1, "DESC")
        self.assertEqual(array,  sorted(array, reverse=True))

    def test_asc_asc(self):
        array = [0, 2, 4, 6, 8, 10]
        quick_sort(array, 0, len(array) - 1, "ASC")
        self.assertEqual(array,  sorted(array))

    def test_desc_asc(self):
        array = [10, 8, 6, 4, 2, 0]
        quick_sort(array, 0, len(array) - 1, "ASC")
        self.assertEqual(array,  sorted(array))

    def test_asc_desc(self):
        array = [0, 2, 4, 6, 8, 10]
        quick_sort(array, 0, len(array) - 1, "DESC")
        self.assertEqual(array, sorted(array, reverse=True))

    def test_desc_desc(self):
        array = [10, 8, 6, 4, 2, 0]
        quick_sort(array, 0, len(array) - 1, "DESC")
        self.assertEqual(array, sorted(array, reverse=True))


if __name__ == '__main__':
    unittest.main()
