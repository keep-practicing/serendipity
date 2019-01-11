#!/usr/bin/env python3


class Array:
    def __init__(self, arr=None, capacity: int=0):
        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
            return
        self._data = [None]*capacity
        self._size = 0
    
    def get_size(self) -> int:
        return self._size
    
    def get_capacity(self) -> int:
        return len(self._data)
    
    def is_empty(self) -> bool:
        return self._size == 0

    def add_last(self, e):
        self.add(self._size, e)

    def add_first(self, e):
        self.add(0, e)

    def add(self, index: int, e):
        if index < 0 or index > self._size:
            raise IndexError("Add failed. Require index >= 0 and index < index <= array sise.")
        if self._size == self.get_capacity():
            if self._size == 0:
                self._resize(1)
            else:
                self._resize(2*self.get_capacity())
        for i in range(self._size -1, index-1, -1):
            self._data[i+1] = self._data[i]
        self._data[index] = e
        self._size += 1

    def get(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("Get failed. Index is illegal.")
        return self._data[index]

    def get_first(self):
        if self._size > 0:
            return self._data[0]
    
    def get_last(self):
        if self._size > 0:
            return self._data[self._size-1]

    def set(self, index, e):
        if index < 0 or index >= self._size:
            raise IndexError("Get failed. Index is illegal.")
        self._data[index] = e

    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True
        return False
    
    def find(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    def remove(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Remove failed. Index is illegal.")
        ret = self._data[index]
        for i in range(index+1, self._size):
            self._data[i-1] = self._data[i]
        self._size -= 1

        if self._size == self.get_capacity() // 4 and self.get_capacity() // 2 != 0:  # 防止时间复杂度震荡。
            self._resize(self.get_capacity() // 2)
        return ret
    
    def remove_first(self):
        return self.remove(0)
    
    def remove_last(self):
        return self.remove(self._size-1)

    def remove_element(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)
    
    def __str__(self):
        return f"Array: {self._data[:self._size]}, capacity: {self.get_capacity()}"

    def __repr__(self):
        return self.__str__()

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
