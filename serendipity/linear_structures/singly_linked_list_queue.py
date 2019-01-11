class QueueEmptyException(Exception):
    pass


class SinglyLinkedListQueue:
    class _Node:
        def __init__(self, val=None, next_node=None):
            self.val = val
            self.next = next_node

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        if self._tail is None:
            self._tail = self._Node(val=e)
            self._head = self._tail
        else:
            self._tail.next = self._Node(val=e)
            self._tail = self._tail.next
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException("cannot dequeue from an empty queue.")
        ret = self._head
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return ret.val

    def get_front(self):
        if self.is_empty():
            raise QueueEmptyException("cannot get front from an empty queue.")
        return self._head.val

    def __str__(self):
        res = "Queue: head: "
        cur = self._head
        while cur is not None:
            res += str(cur.val) + "->"
            cur = cur.next
        res += "NULL tail."
        return res

    def __repr__(self):
        return self.__str__()
