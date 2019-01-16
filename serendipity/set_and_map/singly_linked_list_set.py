from serendipity.linear_structures.singly_linked_list import LinkedList


class Set:
    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def contains(self, e):
        return self._list.contains(e)

    def add(self, e):
        if not self._list.contains(e):
            self._list.add_first(e)

    # def remove(self, e):
    #     """借助于链表的移出元素实现即可，此处不实现"""
    #     pass
