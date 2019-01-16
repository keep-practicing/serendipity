import unittest
from serendipity.set_and_map.bst_map import Map


class MapTsetCase(unittest.TestCase):
    def setUp(self):
        self.map = Map()

    def test_map(self):
        self.assertTrue(self.map.is_empty())
        self.assertEqual(self.map.get_size(), 0)

        self.map.add("g", 80)
        self.map.add("f", 81)
        self.map.add("c", 80)
        self.map.add("d", 80)
        self.map.add("h", 80)
        self.map.add("k", 80)
        self.assertEqual(self.map.get_size(), 6)
        self.assertTrue(self.map.contains("d"))
        self.map.set("k", 90)
        self.assertEqual(self.map.get("k"), 90)
        self.map.add("b", 80)
        self.map.add("j", 80)
        self.map.add("m", 80)
        self.map.add("l", 80)
        self.map.add("ca", 80)
        self.assertEqual(self.map.remove("c"), 80)
        self.assertEqual(self.map.remove("j"), 80)
        self.assertEqual(self.map.remove("m"), 80)
        self.assertIsNone(self.map.remove("n"))
