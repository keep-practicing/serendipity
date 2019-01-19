import unittest
from serendipity.tree_structures.priority_queue import PriorityQueue


class PriorityQueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_queue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.enqueue(10)
        self.queue.enqueue(11)
        self.assertEqual(self.queue.get_size(), 4)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.get_front(), 11)
        for i in [11, 10, 6, 5]:
            self.assertEqual(self.queue.dequeue(), i)
