class IllegalArgumentException(Exception):
    pass


class LinkedList:
    class _Node:
        def __init__(self, val=None, next_node=None):
            self.val = val
            self.next = next_node

        # def __str__(self):
        #     return str(self.val)

        # def __repr__(self):
        #     return self.__str__()

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, index, e):
        if index < 0 or index > self._size:
            raise IllegalArgumentException("add failed, illegal index.")
        prev = self._dummy_head
        for _ in range(index):
            prev = prev.next
        prev.next = self._Node(e, prev.next)
        self._size += 1

    def add_first(self, e):
        self.add(0, e)

    def add_last(self, e):
        self.add(self._size, e)

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IllegalArgumentException("get failed, illegal index.")
        cur = self._dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self._size-1)

    def set(self, index, e):
        if index < 0 or index >= self._size:
            raise IllegalArgumentException("set failed, illegal index.")
        cur = self._dummy_head.next
        for _ in range(index):
            cur = cur.next
        cur.val = e

    def contains(self, e):
        cur = self._dummy_head.next
        while cur is not None:
            if cur.val == e:
                return True
            cur = cur.next
        return False

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise IllegalArgumentException("remove failed, illegal index.")
        prev = self._dummy_head
        for _ in range(index):
            prev = prev.next
        ret = prev.next
        prev.next = ret.next
        self._size -= 1
        return ret.val

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size-1)

    def __str__(self):
        res = ""
        cur = self._dummy_head.next
        while cur is not None:
            res += str(cur.val) + "->"
            cur = cur.next
        res += "NULL"
        return res

    def __repr__(self):
        return self.__str__()
