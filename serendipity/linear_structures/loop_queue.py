#!/usr/bin/env python3


class QueueEmpty(Exception):
    pass


class LoopQueue:
    def __init__(self, cap=10):
        self._data = [None] * (cap+1)
        self._front = self._tail = self._size = 0

    def get_capacity(self):
        return len(self._data) - 1  # 循环队列会浪费一个存储空间。

    def is_empty(self):
        return self._front == self._tail

    def get_size(self):
        return self._size

    # time complexity: O(1), 均摊时间复杂度。
    def enqueue(self, e):
        if (self._tail+1) % len(self._data) == self._front:  # 队列满
            self._resize(self.get_capacity()*2)
        self._data[self._tail] = e
        self._tail = (self._tail+1) % len(self._data)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty("Cannot dequeue from an empty queue.")
        ret = self._data[self._front]
        self._front = (self._front+1) % len(self._data)
        self._size -= 1

        if self._size == self.get_capacity() // 4 and self.get_capacity() // 2 != 0:  # 防止复杂度震荡
            self._resize(self.get_capacity() // 2)
        return ret

    def get_front(self):
        if self.is_empty():
            raise QueueEmpty("queue is empty")
        return self._data[self._front]

    def _resize(self, new_capacity):
        new_data = [None] * (new_capacity+1)
        for i in range(self._size):
            new_data[i] = self._data[(i+self._front) % len(self._data)]
        self._data = new_data
        self._front = 0
        self._tail = self._size

    def __str__(self):
        return f"Queue: size = {self._size}, capacity = {self.get_capacity()}, front {[self._data[(i+self._front)%len(self._data)] for i in range(self._size)]} tail."

    def __repr__(self):
        return self.__str__()
