#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 1/28/2019 17:13
# @Author  : fzw
# @FileName: test_segment_tree.py
# @Software: PyCharm


import unittest
from serendipity.tree_structures.segment_tree import SegmentTree


class SegmentTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.segment_tree = SegmentTree(
            [1, 2, 3, 6, 7, 8, 9, 3, 4, 2, 5], lambda a, b: a + b
        )

    def test_segment_tree(self):
        self.assertEqual(self.segment_tree.get_size(), 11)
        self.assertEqual(self.segment_tree.get(3), 6)
        self.assertEqual(self.segment_tree.query(4, 9), 33)
        self.segment_tree.setter(6, 10)
        self.assertEqual(self.segment_tree.query(4, 9), 34)
