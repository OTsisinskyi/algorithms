from quick_sort import quick_sort
import unittest


class TestQuickSort(unittest.TestCase):
    def test_asc(self):
        array = [0, 4, 6, 10, 8, 2]
        self.assertEqual(quick_sort(array, 0, len(array) - 1,  "asc"), [0, 2, 4, 6, 8, 10])

    def test_decs(self):
        array = [0, 4, 6, 10, 8, 2]
        self.assertEqual(quick_sort(array, 0, len(array)-1, "desc"), [10, 8, 6, 4, 2, 0])

    def test_asc_asc(self):
        array = [0, 2, 4, 6, 8, 10]
        self.assertEqual(quick_sort(array, 0, len(array) - 1,  "asc"), [0, 2, 4, 6, 8, 10])

    def test_desc_asc(self):
        array = [10, 8, 6, 4, 2, 0]
        self.assertEqual(quick_sort(array, 0, len(array) - 1,  "asc"), [0, 2, 4, 6, 8, 10])

    def test_asc_desc(self):
        array = [0, 2, 4, 6, 8, 10]
        self.assertEqual(quick_sort(array, 0, len(array) - 1,  "desc"), [10, 8, 6, 4, 2, 0])

    def test_desc_desc(self):
        array = [10, 8, 6, 4, 2, 0]
        self.assertEqual(quick_sort(array, 0, len(array) - 1,  "desc"), [10, 8, 6, 4, 2, 0])


if __name__ == '__main__':
    unittest.main()
