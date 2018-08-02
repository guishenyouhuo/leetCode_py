#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-2 15:45
# @Author  : wangfei
# @File    : TreeProblems.py


import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeProblems:
    """
        给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
        示例 :
        输入:
           1
            \
             3
            /
           2
        输出:
        1
        解释:
        最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
        注意: 树中至少有2个节点
    """

    def get_minimum_difference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        pre_num = -1
        min_sub = sys.maxsize
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                root = t.right
                if pre_num >= 0:
                    new_sub = t.val - pre_num
                    min_sub = new_sub if new_sub < min_sub else min_sub
                pre_num = t.val
        return min_sub


"""
    测试
"""
mp = TreeProblems()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(7)
# root.right.left = TreeNode(2)
print(mp.get_minimum_difference(root))
