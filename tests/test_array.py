import unittest
from serendipity.linear_structures.array import Array


class ArrayTestCase(unittest.TestCase):
    def test_get_size(self):
        array = Array([1, 2, 3])
        self.assertEqual(array.get_size(), 3)

    def test_get_capacity(self):
        array = Array()
        self.assertEqual(array.get_capacity(), 0)
        array.add_last(5)
        self.assertEqual(array.get_capacity(), 1)
        array.add_last(5)
        self.assertEqual(array.get_capacity(), 2)
        array.add_last(5)
        self.assertEqual(array.get_capacity(), 4)
        array.add_last(5)
        self.assertEqual(array.get_capacity(), 4)
        array.add_last(5)
        self.assertEqual(array.get_capacity(), 8)

    def test_is_empty(self):
        array = Array()
        self.assertTrue(array.is_empty())

    def test_add_last_and_get_last(self):
        array = Array()
        array.add_last(6)
        self.assertEqual(array.get_last(), 6)

    def test_add_first_and_get_first(self):
        array = Array()
        array.add_first(6)
        self.assertEqual(array.get_first(), 6)

    def test_add_and_get(self):
        array = Array([1, 2, 3])
        try:
            array.add(6, 4)
        except Exception as e:
            self.assertTrue(isinstance(e, IndexError))
        array.add(1, 5)
        self.assertEqual(array.get(1), 5)
        try:
            array.get(20)
        except Exception as e:
            self.assertTrue(isinstance(e, IndexError))

    def test_contains_and_find(self):
         array = Array([1, 2, 3])
         self.assertTrue(array.contains(3))
         self.assertFalse(array.contains(6))
         self.assertEqual(array.find(2), 1)
         self.assertEqual(array.find(6), -1)

    def test_remove_element(self):
        array = Array([1, 2, 3])
        array.remove_element(2)
        self.assertEqual(array.find(2), -1)

    def test_remove_first(self):
        array = Array([1, 2, 3])
        array.remove_first()
        self.assertEqual(array.find(1), -1)

    def test_remove_last(self):
        array = Array([1, 2, 3])
        array.remove_last()
        self.assertEqual(array.find(3), -1)

    def test_remove(self):
        array = Array([1, 2, 3, 4, 5, 6, 7, 8])
        try:
            array.remove(array.get_size())
        except Exception as e:
            self.assertTrue(isinstance(e, IndexError))
        array.remove_last()
        self.assertEqual(array.get_capacity(), 8)
        array.remove_last()
        self.assertEqual(array.get_capacity(), 8)
        array.remove_last()
        self.assertEqual(array.get_capacity(), 8)
        array.remove_last()
        self.assertEqual(array.get_capacity(), 8)
        array.remove_last()
        self.assertEqual(array.get_capacity(), 8)
        array.remove_last()
        self.assertEqual(array.get_capacity(), 4)
        array.remove_last()
        self.assertEqual(array.get_capacity(), 2)
        array.remove_last()
        self.assertEqual(array.get_capacity(), 1)

    def test_set(self):
        array = Array([1, 2, 3, 4, 5, 6, 7, 8])
        try:
            array.set(array.get_size(), 8)
        except Exception as e:
            self.assertTrue(isinstance(e, IndexError))
        array.set(0, 10)
        self.assertEqual(array.get_first(), 10)

    def test_magic_str(self):
        array = Array([1, 2, 3])
        self.assertEqual(array.__str__(), "Array: [1, 2, 3], capacity: 3")

    def test_magic_repr(self):
        array = Array([1, 2, 3])
        self.assertEqual(array.__repr__(), "Array: [1, 2, 3], capacity: 3")


if __name__ == "__main__":
    unittest.main()
