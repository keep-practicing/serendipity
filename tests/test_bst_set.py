import unittest
from serendipity.set_and_map.bst_set import Set


class SetTestCase(unittest.TestCase):
    def setUp(self):
        self.set = Set()

    def test_set(self):
        self.assertTrue(self.set.is_empty())
        self.set.add(5)
        self.set.add(5)
        self.assertEqual(self.set.get_size(), 1)
        self.assertFalse(self.set.is_empty())
        self.assertTrue(self.set.contains(5))
        self.set.remove(5)
        self.assertFalse(self.set.contains(5))
