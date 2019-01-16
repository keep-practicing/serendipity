import unittest
from serendipity.linear_structures.singly_linked_list import (
    LinkedList,
    IllegalArgumentException,
)


class LinkedListTestCase(unittest.TestCase):
    def test_add_size_empty_get_contains(self):
        linked = LinkedList()
        try:
            linked.add(2, 4)
        except Exception as e:
            self.assertTrue(e, IllegalArgumentException)
        linked.add_first(1)
        linked.add_last(2)
        linked.add(1, 3)
        self.assertEqual(linked.get_size(), 3)
        self.assertFalse(linked.is_empty())
        try:
            linked.get(6)
        except Exception as e:
            self.assertTrue(e, IllegalArgumentException)

        self.assertEqual(linked.get_first(), 1)
        self.assertEqual(linked.get(1), 3)
        self.assertEqual(linked.get_last(), 2)

        self.assertFalse(linked.contains(6))
        self.assertTrue(linked.contains(2))

        try:
            linked.set(5, 3)
        except Exception as e:
            self.assertTrue(e, IllegalArgumentException)

        linked.set(2, 6)
        self.assertEqual(linked.__str__(), "1->3->6->NULL")
        self.assertEqual(linked.__repr__(), "1->3->6->NULL")

        try:
            linked.remove(6)
        except Exception as e:
            self.assertTrue(e, IllegalArgumentException)

        linked.remove_last()
        self.assertEqual(linked.__str__(), "1->3->NULL")
        self.assertEqual(linked.__repr__(), "1->3->NULL")

        linked.remove_first()
        self.assertEqual(linked.__str__(), "3->NULL")
        self.assertEqual(linked.__repr__(), "3->NULL")
