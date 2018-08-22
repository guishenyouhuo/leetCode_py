#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-2 15:45
# @Author  : wangfei
# @File    : TreeProblems.py


import sys
import queue


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

    """
    给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
    示例 :
    给定二叉树
              1
             / \
            2   3
           / \     
          4   5    
    返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
    注意：两结点之间的路径长度是以它们之间边的数目表示。
    """

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        main_len = self.tree_depth(root.left) + self.tree_depth(root.right)
        left_len = self.diameterOfBinaryTree(root.left)
        right_len = self.diameterOfBinaryTree(root.right)
        return max(left_len, right_len, main_len)

    def tree_depth(self, root):
        """
        树的深度
        :param root:
        :return:
        """
        if root is None:
            return 0
        return max(1 + self.tree_depth(root.left), 1 + self.tree_depth(root.right))

    """
        根据数组创建二叉树
    """
    def array_to_tree(self, root_arr):
        """
        根据数组创建二叉树
        :param root_arr: 数组
        :return:
        """
        if root_arr is None or len(root_arr) == 0:
            return None
        root = TreeNode(root_arr[0])
        tree_queue = queue.Queue()
        tree_queue.put(root)
        for idx in range(1, len(root_arr), 2):
            node = tree_queue.get()
            if node is None:
                continue
            left_val = root_arr[idx]
            idx += 1
            if idx < len(root_arr):
                right_val = root_arr[idx]
            if left_val is not None:
                node.left = TreeNode(left_val)
                tree_queue.put(node.left)
            if right_val is not None:
                node.right = TreeNode(right_val)
                tree_queue.put(node.right)
        return root

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
if __name__ == "__main__":
    mp = TreeProblems()
    root_arr = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None,
                None, -1, -4, None, None, None, -2]
    root = mp.array_to_tree(root_arr)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(2)
    # print(mp.get_minimum_difference(root))
    mp.inOrderTree(root)
    # mp.inOrderTree(mp.convertBST(root))
    print(mp.diameterOfBinaryTree(root))
