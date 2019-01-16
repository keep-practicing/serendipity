class Map:
    class _Node:
        def __init__(self, key=None, value=None, next_node=None):
            self.key = key
            self.value = value
            self.next = next_node
    
    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_node(self, key):
        cur = self._dummy_head.next
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def contains(self, key):
        return self.get_node(key) is not None

    def get(self, key):
        node = self.get_node(key)
        return None if node is None else node.value

    def add(self, key, val):
        node = self.get_node(key)
        if node is None:
            self._dummy_head.next = self._Node(key=key, value=val, next_node=self._dummy_head.next)
            self._size += 1
        else:
            node.value = val

    def set(self, key, val):
        self.add(key, val)

    def remove(self, key):
        prev = self._dummy_head
        while prev.next is not None:
            if prev.next.key == key:
                break
            prev = prev.next
        if prev.next is not None:
            ret = prev.next.value
            prev.next = prev.next.next
            self._size -= 1
            return ret
        return 
