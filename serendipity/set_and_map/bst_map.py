from dataclasses import dataclass
from typing import Any


@dataclass(init=False)
class Map:
    @dataclass
    class _Node:
        key: Any  # can be compare
        value: Any
        left = None
        right = None

    _root = None
    _size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, key, val):
        self._root = self._add(self._root, key, val)

    def _add(self, node, key, val):
        if node is None:
            self._size += 1
            return self._Node(key, val)
        if key < node.key:
            node.left = self._add(node.left, key, val)
        elif key > node.key:
            node.right = self._add(node.right, key, val)
        else:
            node.value = val
        return node

    def _get_node(self, node, key):
        if node is None:
            return
        if key == node.key:
            return node
        elif key < node.key:
            return self._get_node(node.left, key)
        else:
            return self._get_node(node.right, key)

    def contains(self, key):
        return self._get_node(self._root, key) is not None

    def get(self, key):
        node = self._get_node(self._root, key)
        return None if node is None else node.value

    def set(self, key, val):
        self.add(key, val)

    def _minimum(self, node):
        if node.left is None:
            return node
        return self._minimum(node.left)

    def _remove_min(self, node):
        if node.left is None:
            self._size -= 1
            return node.right
        node.left = self._remove_min(node.left)
        return node

    def remove(self, key):
        node = self._get_node(self._root, key)
        if node is not None:
            self._root = self._remove(self._root, key)
            return node.value
        return

    def _remove(self, node, key):
        if node is None:
            return
        if key < node.key:
            node.left = self._remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            return node
        else:
            if node.left is None:
                self._size -= 1
                return node.right
            if node.right is None:
                self._size -= 1
                return node.left
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left
            return successor
