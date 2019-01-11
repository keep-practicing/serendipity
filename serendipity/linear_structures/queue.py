#!/usr/bin/env python3
from serendipity.linear_structures.array import Array


class ArrayQueue:
    def __init__(self, cap=0):
        self._array = Array(capacity=cap)

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def enqueue(self, e):
        self._array.add_last(e)

    def dequeue(self):  # time complexity: O(n)
        return self._array.remove_first()

    def get_front(self):
        return self._array.get_first()

    def __str__(self):
        return f"ArrayQueue: front {[self._array.get(i) for i in range(self.get_size())]} tail."

    def __repr__(self):
        return self.__str__()
