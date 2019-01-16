from dataclasses import dataclass
from typing import Any


class IllegalArgumentException(Exception):
    pass


@dataclass(init=False)
class BST:
    """
    此二分搜索树不包含重复元素
    """

    @dataclass
    class _Node:
        val: Any  # can be compare
        left = None
        right = None

    _root = None
    _size: int = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        self._root = self._add(self._root, e)

    def _add(self, node, e: Any):
        if node is None:
            self._size += 1
            return self._Node(val=e)
        if e < node.val:
            node.left = self._add(node.left, e)
        elif e > node.val:
            node.right = self._add(node.right, e)
        return node

    def contains(self, e):
        return self._contains(self._root, e)

    def _contains(self, node, e):
        if node is None:
            return False
        if node.val == e:
            return True
        elif e < node.val:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right, e)

    def minimum(self):
        if self._size == 0:
            raise IllegalArgumentException("bst is empty!")
        return self._minimum(self._root).val

    def _minimum(self, node):
        if node.left is None:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self._size == 0:
            raise IllegalArgumentException("bst is empty!")
        return self._maximum(self._root).val

    def _maximum(self, node):
        if node.right is None:
            return node
        return self._maximum(node.right)

    def remove_min(self):
        res = self.minimum()
        self._root = self._remove_min(self._root)
        return res

    def _remove_min(self, node):
        if node.left is None:
            self._size -= 1
            return node.right
        node.left = self._remove_min(node.left)
        return node

    def remove_max(self):
        res = self.maximum()
        self._root = self._remove_max(self._root)
        return res

    def _remove_max(self, node):
        if node.right is None:
            self._size -= 1
            return node.left
        node.right = self._remove_max(node.right)
        return node

    def remove(self, e):
        self._root = self._remove(self._root, e)

    def _remove(self, node, e):
        if node is None:
            return
        if e < node.val:
            node.left = self._remove(node.left, e)
            return node
        elif e > node.val:
            node.right = self._remove(node.right, e)
            return node
        else:
            if node.left is None:
                self._size -= 1
                return node.right
            if node.right is None:
                self._size -= 1
                return node.left

            # 左右子树🌲都不为空，找到要删除节点右子树的最小节点, 也可以是左子树的最大节点。
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left
            return successor
