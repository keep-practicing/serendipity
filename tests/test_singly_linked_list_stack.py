import unittest
from serendipity.linear_structures.singly_linked_list_stack import LinkedListStack


class LinkedListStackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = LinkedListStack()

    def test_stack_all_operate(self):
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.get_size(), 1)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertTrue(self.stack.is_empty())
