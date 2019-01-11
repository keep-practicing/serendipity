from serendipity.linear_structures.linked_list import LinkedList


class LinkedListStack:
    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def push(self, e):
        self._list.add_first(e)

    def pop(self):
        return self._list.remove_first()

    def peek(self):
        return self._list.get_first()
