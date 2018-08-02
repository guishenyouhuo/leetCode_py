#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-7-30 11:01
# @Author  : wangfei
# @File    : MathProbelms.py

import math


class MathProblem:
    """
        对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
        给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False
        示例：
        输入: 28
        输出: True
        解释: 28 = 1 + 2 + 4 + 7 + 14
        注意:
        输入的数字 n 不会超过 100,000,000. (1e8)
    """
    @staticmethod
    def check_perfect_number(num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sq = int(math.sqrt(num))
        ans = 1
        for i in range(2, sq + 1):
            if num % i == 0:
                ans += i + num / i
        return ans == num

    """
        给定一个单词，你需要判断单词的大写使用是否正确。
        我们定义，在以下情况时，单词的大写用法是正确的：
        全部字母都是大写，比如"USA"。
        单词中所有字母都不是大写，比如"leetcode"。
        如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
        否则，我们定义这个单词没有正确使用大写字母。
        示例 1:
        输入: "USA"
        输出: True
        示例 2:
        输入: "FlaG"
        输出: False
        注意: 输入是由大写和小写拉丁字母组成的非空单词。
    """
    @staticmethod
    def detect_capital_use(word):
        """
        :type word: str
        :rtype: bool
        """
        first_upper = word[0].isupper()
        word_len = len(word)
        upper_count = 1 if first_upper else 0
        for i in range(1, word_len):
            cur_upper = word[i].isupper()
            if cur_upper:
                upper_count += 1
                if not first_upper:
                    return False
        if first_upper and (upper_count == 1 or upper_count == word_len):
            return True
        if not first_upper and upper_count == 0:
            return True
        return False

    """
        给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
        子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。
        输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。
        示例 :
        输入: "aba", "cdc"
        输出: 3
        解析: 最长特殊序列可为 "aba" (或 "cdc")
        说明:
        两个字符串长度均小于100。
        字符串中的字符仅含有 'a'~'z'。
    """
    @staticmethod
    def find_lus_length(a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        if len(a) >= len(b):
            return len(a)
        else:
            return len(b)


'''测试'''
# print(MathProblem.check_perfect_number(29))
# print(MathProblem.detect_capital_use("gooGle"))
# print(MathProblem.find_lus_length("aba", "cdc"))
mp = MathProblem()
# root = TreeNode(1)
# mp.get_minimum_difference(root)
