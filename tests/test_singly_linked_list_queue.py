import unittest
from serendipity.linear_structures.singly_linked_list_queue import (
    SinglyLinkedListQueue,
    QueueEmptyException,
)


class SinglyLinkedListQueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = SinglyLinkedListQueue()

    def test_queue_all_operate(self):
        try:
            self.queue.dequeue()
        except Exception as e:
            self.assertTrue(isinstance(e, QueueEmptyException))

        try:
            self.queue.get_front()
        except Exception as e:
            self.assertTrue(isinstance(e, QueueEmptyException))

        for i in range(10):
            self.queue.enqueue(i + 1)
        self.assertEqual(self.queue.get_size(), 10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.get_front(), 1)
        self.assertEqual(
            self.queue.__str__(),
            "Queue: head: 1->2->3->4->5->6->7->8->9->10->NULL tail.",
        )
        self.assertEqual(
            self.queue.__repr__(),
            "Queue: head: 1->2->3->4->5->6->7->8->9->10->NULL tail.",
        )

        for i in range(10):
            self.assertEqual(self.queue.dequeue(), i + 1)
