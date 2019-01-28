class SegmentTree:
    """线段树相当于将数组用一棵树重新表示."""

    def __init__(self, arr, merger):
        self._data = arr[:]
        self._tree = [None] * 4 * len(arr)
        self._merger = merger
        self._build_segment_tree(tree_index=0, left=0, right=len(self._data) - 1)

    def _build_segment_tree(self, tree_index, left, right):
        """在tree_index位置创建表示区间[l...r]的线段树"""
        if left == right:
            self._tree[tree_index] = self._data[left]
            return

        left_tree_index = 2 * tree_index + 1
        right_tree_index = 2 * tree_index + 2

        mid = left + (right - left) // 2
        self._build_segment_tree(left_tree_index, left, mid)
        self._build_segment_tree(right_tree_index, mid + 1, right)
        self._tree[tree_index] = self._merger(
            self._tree[left_tree_index], self._tree[right_tree_index]
        )

    def get_size(self):
        return len(self._data)

    def get(self, index):
        """
        :param index: int, must be valid, 0 <= index < len(self._data)
        :return:
        """
        return self._data[index]

    def query(self, query_l, query_r):
        """
        返回区间[query_l, query_r]的值。
        :param query_l: int, must be valid.
        :param query_r: int, must be valid.
        :return:
        """
        return self._query(0, 0, len(self._data) - 1, query_l, query_r)

    def _query(self, tree_index, left, right, query_l, query_r):
        """
        在以tree_index为根的线段树中[left...right]的范围里，搜索区间[query_l...query_r]的值。
        """
        if left == query_l and right == query_r:
            return self._tree[tree_index]
        mid = left + (right - left) // 2
        left_tree_index = 2 * tree_index + 1
        right_tree_index = 2 * tree_index + 2

        if query_l >= mid + 1:
            return self._query(right_tree_index, mid + 1, right, query_l, query_r)
        elif query_r <= mid:
            return self._query(left_tree_index, left, mid, query_l, query_r)
        else:
            return self._merger(
                self._query(right_tree_index, mid + 1, right, mid + 1, query_r),
                self._query(left_tree_index, left, mid, query_l, mid),
            )

    def setter(self, index, e):
        """
        将index位置的值，更新为e
        :param index: int, must be valid.
        :param e:
        :return:
        """
        self._data[index] = e
        self._setter(0, 0, len(self._data) - 1, index, e)

    def _setter(self, tree_index, left, right, index, e):
        """
        在以tree index为根的线段树中更新index的值为e
        """
        if left == right:
            self._tree[tree_index] = e
            return
        mid = left + (right - left) // 2
        left_tree_index = 2 * tree_index + 1
        right_tree_index = 2 * tree_index + 2
        if index >= mid + 1:
            self._setter(right_tree_index, mid + 1, right, index, e)
        else:  # index <= mid
            self._setter(left_tree_index, left, mid, index, e)
        self._tree[tree_index] = self._merger(
            self._tree[left_tree_index], self._tree[right_tree_index]
        )
