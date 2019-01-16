from serendipity.tree_structures.bst import BST


class Set:
    def __init__(self):
        self._bst = BST()

    def get_size(self):
        return self._bst.size()

    def is_empty(self):
        return self._bst.is_empty()

    def add(self, e):
        self._bst.add(e)

    def contains(self, e):
        return self._bst.contains(e)

    def remove(self, e):
        self._bst.remove(e)
