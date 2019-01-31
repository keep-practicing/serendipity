#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 1/31/19 10:09
# @Author  : fzw
# @FileName: trie.py
# @Software: PyCharm


class Trie:
    class _Node:
        def __init__(self, is_word: bool = False):
            self.is_word = is_word
            self.next = {}

    def __init__(self):
        self._root = self._Node()
        self._size: int = 0

    def get_size(self):
        return self._size

    def add(self, word: str):
        """向trie中添加新的单词"""
        cur = self._root
        for i in word:
            if cur.next.get(i) is None:
                cur.next[i] = self._Node()
            cur = cur.next.get(i)

        if not cur.is_word:
            cur.is_word = True
            self._size += 1

    def contains(self, word: str):
        """查询单词word是否在trie中"""
        cur = self._root
        for i in word:
            if cur.next.get(i) is None:
                return False
            cur = cur.next.get(i)
        return cur.is_word

    def is_prefix(self, prefix: str):
        """查询在trie中是否有以prefix为前缀的单词"""
        cur = self._root
        for i in prefix:
            if cur.next.get(i) is None:
                return False
            cur = cur.next.get(i)
        return True
