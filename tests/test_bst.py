import unittest
from serendipity.tree_structures.bst import BST, IllegalArgumentException


class BSTTestCase(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_bst(self):
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(self.bst.size(), 0)
        try:
            self.bst.minimum()
        except Exception as e:
            self.assertTrue(isinstance(e, IllegalArgumentException))
        try:
            self.bst.maximum()
        except Exception as e:
            self.assertTrue(isinstance(e, IllegalArgumentException))
        self.bst.add(6)
        self.bst.add(3)
        self.bst.add(8)
        self.bst.add(9)
        self.assertTrue(self.bst.contains(9))
        self.assertFalse(self.bst.contains(7))
        self.assertEqual(self.bst.minimum(), 3)
        self.assertEqual(self.bst.maximum(), 9)
        self.assertEqual(self.bst.remove_min(), 3)
        self.assertEqual(self.bst.minimum(), 6)
        self.assertEqual(self.bst.remove_max(), 9)
        self.assertEqual(self.bst.maximum(), 8)
        self.bst.add(3)
        self.bst.add(2)
        self.bst.add(4)
        self.bst.add(7)
        self.bst.add(9)
        self.bst.add(1)
        self.bst.add(5)
        self.bst.remove(2)
        self.assertFalse(self.bst.contains(2))
        self.bst.remove(4)
        self.assertFalse(self.bst.contains(4))
        self.bst.remove(8)
        self.assertFalse(self.bst.contains(8))
        self.bst.remove(10)
