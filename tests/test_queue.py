import unittest
from serendipity.linear_structures.queue import ArrayQueue


class ArrayQueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = ArrayQueue()

    def test_queue_all_operate(self):
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.__str__(), "ArrayQueue: front [4, 5] tail.")
        self.assertEqual(self.queue.__repr__(), "ArrayQueue: front [4, 5] tail.")
        self.assertEqual(self.queue.get_size(), 2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.get_front(), 4)
        self.assertEqual(self.queue.dequeue(), 4)
