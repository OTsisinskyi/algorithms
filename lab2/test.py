import unittest
from HashTable import HashTable


class TestHashTable(unittest.TestCase):

    def test_set_func(self):
        hash_table = HashTable()
        self.assertEqual(hash_table.set("Alex", 1000), [("Alex", 1000)])

    def test_get_func(self):
        hash_table = HashTable()
        hash_table.set("Alex", 1000)
        self.assertEqual(hash_table.get("Alex"), [("Alex", 1000)])

    def test_delete_func(self):
        hash_table = HashTable()
        hash_table.set("Alex", 1000)
        self.assertEqual(hash_table.delete("Alex"), "Alex")
