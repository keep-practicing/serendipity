import unittest
from serendipity.tree_structures.trie import Trie


class TrieTestCase(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_trie(self):
        self.assertEqual(self.trie.get_size(), 0)
        self.trie.add("hello")
        self.trie.add("head")
        self.trie.add("he")
        self.assertEqual(self.trie.get_size(), 3)
        self.assertFalse(self.trie.contains("hi"))
        self.assertTrue(self.trie.contains("he"))
        self.assertTrue(self.trie.is_prefix("he"))
        self.assertFalse(self.trie.is_prefix("la"))


if __name__ == "__main__":
    unittest.main()
