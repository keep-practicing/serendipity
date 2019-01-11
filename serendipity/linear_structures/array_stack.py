#!/usr/bin/env python3
from serendipity.linear_structures.array import Array


class ArrayStack:
    def __init__(self, cap=0):
        self._array = Array(capacity=cap)

    def push(self, e):
        self._array.add_last(e)

    def pop(self):
        return self._array.remove_last()

    def peek(self):
        return self._array.get_last()

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self._array.get_capacity()

    def __str__(self):
        return f"ArrayStack: {[self._array.get(i) for i in range(self.get_size())]}, right is top."

    def __repr__(self):
        return self.__str__()
