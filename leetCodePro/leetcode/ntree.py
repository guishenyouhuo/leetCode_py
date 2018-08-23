#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/23 0023 下午 10:18
# @Author  : Administrator
# @File    : ntree.py


from queue import Queue


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth1(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        q = Queue()
        q.put(root)
        deepth = 1
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(0, size):
                node = q.get()
                child_list = node.children
                if child_list is None:
                    continue
                for child in child_list:
                    if child is not None:
                        q.put(child)
                deepth += 1
        return deepth

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)


if __name__ == "__main__":
    so = Solution()
    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)
    root = Node(1, [node3, node2, node4])
    print(so.maxDepth(root))
