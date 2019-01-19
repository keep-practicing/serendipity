import unittest
import numpy as np
from serendipity.tree_structures.max_heap import MaxHeap


class MaxHeapTestCase(unittest.TestCase):
    def setUp(self):
        arr = np.arange(100)
        np.random.shuffle(arr)
        self.test_data = list(arr)
        self.heap = MaxHeap()

    def test_max_heap_with_heapify(self):
        heap = MaxHeap(self.test_data)
        self.assertEqual(heap.size(), 100)
        self.assertFalse(heap.is_empty())
        heap_data = [heap.extract_max() for _ in range(heap.size())]

        for i in range(1, heap.size()):
            self.assertGreater(heap_data[i], heap_data[i-1])

    def test_max_heap_without_heapify(self):
        for i in self.test_data:
            self.heap.add(i)

        self.heap.replace(200)

        heap_data = [self.heap.extract_max() for _ in range(self.heap.size())]
        self.assertEqual(heap_data[0], 200)
        for i in range(1, self.heap.size()):
            self.assertGreater(heap_data[i], heap_data[i-1])
