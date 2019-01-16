import unittest
from serendipity.set_and_map.singly_linked_list_map import Map


class MapTestCase(unittest.TestCase):
    def setUp(self):
        self.map = Map()

    def test_map(self):
        self.map.add("a", 65)
        self.assertEqual(self.map.get_size(), 1)
        self.assertFalse(self.map.is_empty())
        self.assertTrue(self.map.contains("a"))
        self.map.set("a", 66)
        self.assertTrue(self.map.contains("a"))
        self.map.add("b", 23)
        self.map.add("c", 22)
        self.assertEqual(self.map.remove("b"), 23)
        self.assertIsNone(self.map.remove("n"))
        self.assertEqual(self.map.get("a"), 66)
