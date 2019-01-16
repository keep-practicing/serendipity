import unittest
from serendipity.linear_structures.loop_queue import LoopQueue, QueueEmpty


class LoopQueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = LoopQueue()

    def test_loop_queue_all_operate(self):
        try:
            self.queue.dequeue()
        except Exception as e:
            self.assertTrue(isinstance(e, QueueEmpty))

        try:
            self.queue.get_front()
        except Exception as e:
            self.assertTrue(isinstance(e, QueueEmpty))

        for i in range(10):
            self.queue.enqueue(i + 1)
        self.assertEqual(self.queue.get_capacity(), 10)
        self.assertEqual(self.queue.get_size(), 10)
        self.assertFalse(self.queue.is_empty())
        self.queue.enqueue(11)
        self.assertEqual(self.queue.get_capacity(), 20)
        self.assertEqual(self.queue.get_size(), 11)
        self.assertEqual(self.queue.get_front(), 1)
        self.assertEqual(
            self.queue.__str__(),
            "Queue: size = 11, capacity = 20, front [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] tail.",
        )
        self.assertEqual(
            self.queue.__repr__(),
            "Queue: size = 11, capacity = 20, front [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] tail.",
        )
        for i in range(5):
            self.queue.dequeue()
        self.assertEqual(self.queue.get_capacity(), 20)
        self.assertEqual(self.queue.get_size(), 6)
        self.queue.dequeue()
        self.assertEqual(self.queue.get_capacity(), 10)
        self.assertEqual(self.queue.get_size(), 5)
