#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2/13/19 14:36
# @Author  : fzw
# @FileName: union_find.py
# @Software: PyCharm


class UF:
    def is_connected(self, p, q):
        raise NotImplementedError

    def union_elements(self, p, q):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError


class UnionFind1(UF):
    def __init__(self, size: int):
        self._id = [i for i in range(size)]

    def get_size(self):
        return len(self._id)

    def _find(self, p: int):
        """查找元素p所对应的集合编号。"""
        # 此处需要对p进行合法性检查
        return self._id[p]

    # time complexity O(1)
    def is_connected(self, p: int, q: int):
        """查看元素p和q是否所属一个集合"""
        return self._find(p) == self._find(q)

    # time complexity O(n)
    def union_elements(self, p: int, q: int):
        p_id = self._find(p)
        q_id = self._find(q)
        if p_id == q_id:
            return

        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id


class UnionFind2(UF):
    def __init__(self, size: int):
        self._parent = [i for i in range(size)]
        self._sz = [1 for _ in range(size)]  # 基于size对并查集优化

    def get_size(self):
        return len(self._parent)

    def _find(self, p: int):
        """查找元素p所对应的集合编号, O(h)时间复杂度，h为树的高度。"""
        # p需要进行合法性检查。
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def is_connected(self, p: int, q: int):
        """查找元素p和元素q是否所属一个集合, O(h)时间复杂度，h为树的高度。"""
        return self._find(p) == self._find(q)

    def union_elements(self, p: int, q: int):
        """合并元素p和q所属的集合，O(h)时间复杂度，h为树的高度。"""
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return
        if self._sz[p_root] < self._sz[q_root]:
            self._parent[p_root] = q_root
            self._sz[q_root] += self._sz[p_root]
        else:
            self._parent[q_root] = self._parent[p_root]
            self._sz[p_root] += self._sz[q_root]


class UnionFind3(UF):
    def __init__(self, size: int):
        self._parent = [i for i in range(size)]
        self._rank = [1 for _ in range(size)]  # 基于rank对并查集优化

    def get_size(self):
        return len(self._parent)

    def _find(self, p: int):
        """查找元素p所对应的集合编号, O(h)时间复杂度，h为树的高度。"""
        # p需要进行合法性检查。
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def is_connected(self, p: int, q: int):
        """查找元素p和元素q是否所属一个集合, O(h)时间复杂度，h为树的高度。"""
        return self._find(p) == self._find(q)

    def union_elements(self, p: int, q: int):
        """合并元素p和q所属的集合，O(h)时间复杂度，h为树的高度。"""
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[q_root] < self._rank[p_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[q_root] = p_root
            self._rank[p_root] += 1


class UnionFind4(UF):
    def __init__(self, size: int):
        self._parent = [i for i in range(size)]
        self._rank = [1 for _ in range(size)]  # 基于rank对并查集优化

    def get_size(self):
        return len(self._parent)

    def _find(self, p: int):
        """查找元素p所对应的集合编号, O(h)时间复杂度，h为树的高度。"""
        # p需要进行合法性检查。
        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]]  # 路径压缩。
            p = self._parent[p]
        return p

    def is_connected(self, p: int, q: int):
        """查找元素p和元素q是否所属一个集合, O(h)时间复杂度，h为树的高度。"""
        return self._find(p) == self._find(q)

    def union_elements(self, p: int, q: int):
        """合并元素p和q所属的集合，O(h)时间复杂度，h为树的高度。"""
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[q_root] < self._rank[p_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[q_root] = p_root
            self._rank[p_root] += 1


class UnionFind5(UF):
    def __init__(self, size: int):
        self._parent = [i for i in range(size)]
        self._rank = [1 for _ in range(size)]  # 基于rank对并查集优化

    def get_size(self):
        return len(self._parent)

    def _find(self, p: int):
        """查找元素p所对应的集合编号, O(h)时间复杂度，h为树的高度。"""
        # p需要进行合法性检查。
        if p != self._parent[p]:
            self._parent[p] = self._find(self._parent[p])  # 利用递归进行路径压缩。
        return self._parent[p]

    def is_connected(self, p: int, q: int):
        """查找元素p和元素q是否所属一个集合, O(h)时间复杂度，h为树的高度。"""
        return self._find(p) == self._find(q)

    def union_elements(self, p: int, q: int):
        """合并元素p和q所属的集合，O(h)时间复杂度，h为树的高度。"""
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[q_root] < self._rank[p_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[q_root] = p_root
            self._rank[p_root] += 1
