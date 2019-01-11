import unittest
from serendipity.linear_structures.array_stack import ArrayStack


class ArrayStackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = ArrayStack()
    
    def test_stack_all_operate(self):
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.__str__(), "ArrayStack: [2], right is top.")
        self.assertEqual(self.stack.__repr__(), "ArrayStack: [2], right is top.")
        self.assertEqual(self.stack.get_size(), 1)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.get_capacity(), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertTrue(self.stack.is_empty())
