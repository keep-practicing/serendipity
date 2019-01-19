from serendipity.linear_structures.array import Array


class MaxHeap:
    def __init__(self, arr=None, capacity=0):
        if isinstance(arr, list):
            self._data = Array(arr)
            # heapify
            for i in range((self.size() - 1) // 2, -1, -1):
                self._sift_down(i)
        else:
            self._data = Array(capacity=capacity) if capacity else Array()

    def size(self):
        return self._data.get_size()

    def is_empty(self):
        return self._data.is_empty()

    def add(self, e):
        self._data.add_last(e)
        self._sift_up(self.size() - 1)

    def _sift_up(self, index):
        while index > 0 and self._data.get(index) > self._data.get((index - 1) // 2):
            self._data.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def find_max(self):
        if self.size() > 0:
            return self._data.get_first()

    def extract_max(self):
        res = self.find_max()
        self._data.swap(0, self.size() - 1)
        self._data.remove_last()
        self._sift_down(0)
        return res

    def _sift_down(self, index):
        while 2 * index + 1 < self.size():
            j = 2 * index + 1
            if j + 1 < self.size() and self._data.get(j) < self._data.get(j + 1):
                j += 1
            if self._data.get(index) >= self._data.get(j):
                break
            self._data.swap(j, index)
            index = j

    def replace(self, e):
        res = self.find_max()
        self._data.set(0, e)
        self._sift_down(0)
        return res
