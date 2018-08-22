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


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


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
        给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
        例如：
        输入: 二叉搜索树:
                      5
                    /   \
                   2     13
        输出: 转换为累加树:
                     18
                    /   \
                  20     13
        解法：按照右->根_>左的顺序进行遍历，值一直往前累加
    """
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        result = root
        stack = []
        preNum = 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            if stack:
                t = stack.pop()
                tVal = t.val
                t.val = tVal + preNum
                preNum += tVal
                root = t.left
        return result

    """
        树的中序遍历方法
    """
    def inOrderTree(self, root):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                print(t.val, end=" ")
                root = t.right
        print()

    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        else:
            tLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            tRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                return Node(tLeft.val, True, None, None, None, None)
            else:
                return Node(False, False, tLeft, tRight, bLeft, bRight)


"""
    测试
"""
mp = TreeProblems()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
# root.right.left = TreeNode(2)
# print(mp.get_minimum_difference(root))
mp.inOrderTree(root)
mp.inOrderTree(mp.convertBST(root))
