import unittest
from serendipity.tree_structures.union_find import (
    UnionFind1,
    UnionFind2,
    UnionFind3,
    UnionFind4,
    UnionFind5,
)


class UnionFindTestCase(unittest.TestCase):
    def setUp(self):
        self.size = 6
        self.uf1 = UnionFind1(self.size)
        self.uf2 = UnionFind2(self.size)
        self.uf3 = UnionFind3(self.size)
        self.uf4 = UnionFind4(self.size)
        self.uf5 = UnionFind5(self.size)

    def test_union_find(self):
        for i in range(1, self.size):
            for uf in [self.uf1, self.uf2, self.uf3, self.uf4, self.uf5]:
                uf.union_elements(i, i - 1)
                self.assertEqual(uf.get_size(), self.size)
                self.assertTrue(uf.is_connected(i, i - 1))

        for uf in [self.uf1, self.uf2, self.uf3, self.uf4, self.uf5]:
            uf.union_elements(0, 1)
            self.assertEqual(uf.get_size(), self.size)
            self.assertTrue(uf.is_connected(0, 1))


if __name__ == "__main__":
    unittest.main()
