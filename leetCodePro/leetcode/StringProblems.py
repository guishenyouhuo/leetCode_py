#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/4 0004 上午 11:14
# @Author  : Administrator
# @File    : StringProblems.py


class StringProblems:

    """
        给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。
        如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
        示例:
        输入: s = "abcdefg", k = 2
        输出: "bacdfeg"
        要求:
        该字符串只包含小写的英文字母。
        给定字符串的长度和 k 在[1, 10000]范围内。
    """
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        strLen = len(s)
        group = int(strLen / (2 * k))
        remain = strLen % (2 * k)
        chList = list(s)
        for i in range(0, group):
            begin = i * 2 * k
            end = begin + k - 1
            while begin < end:
                chList[begin], chList[end] = chList[end], chList[begin]
                begin += 1
                end -= 1
        if remain == 0:
            return "".join(chList)
        reminLen = remain if remain < k else k
        begin = group * 2 * k
        end = begin + reminLen - 1
        while begin < end:
            chList[begin], chList[end] = chList[end], chList[begin]
            begin += 1
            end -= 1
        return "".join(chList)

    """
        给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：
        'A' : Absent，缺勤
        'L' : Late，迟到
        'P' : Present，到场
        如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
        你需要根据这个学生的出勤纪录判断他是否会被奖赏。
        示例 1:
        输入: "PPALLP"
        输出: True
        示例 2:
        输入: "PPALLL"
        输出: False
    """
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent_num = 0
        max_conti_late = 0
        for ch in s:
            if ch == 'A':
                absent_num += 1
                max_conti_late = 0
            elif ch == 'L':
                max_conti_late += 1
            else:
                max_conti_late = 0
            if absent_num > 1:
                return False
            if max_conti_late > 2:
                return False
        return True

    """
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
    示例 1:
    输入: "Let's take LeetCode contest"
    输出: "s'teL ekat edoCteeL tsetnoc" 
    注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s.split()
        res = []
        for item in ans:
            res.append(item[::-1])
        return ' '.join(res)


"""
    测试
"""
if __name__ == "__main__":
    sp = StringProblems()
    # print(sp.reverseStr("uxzpsogzkwgwacxxvvzlhkaahjaqagdfjkmyutvhxclzskvxckjvfgzptlzldjwhrpocfugzqkpaxexezbvggtkoxriysqivup"
    #                     "ofrcoxbrdgccvphvdtvrjtsbospmgyfduvaslnvxwuepleziodaaqmonsxjszyjwjmvgdqgowjjtwdmynvirnlujimedfyntgacn"
    #                     "tvyqujvehhvruiolfkeprqpzdvmapeukemmzxdtyolxeixatgsupvpidmeyifjyxkzudxvsunghtklzgxsjhrxgxgqcdebukrarpk"
    #                     "pqmusempvulagashxpaisfvetrmiqiordsyjgyjmkvavxorrmnxbiikuxmezpkhgkjzmapldnmjvfxtmckskiwhdnuqpqrsrdspxuix"
    #                     "xnibjxoyagijmlbhjtuchzbdpaxommfvlbpxfnzkkcdentdhhxracunvrtqxrbqanufaglncjqiwofanuznfmbtjalehlqidtcmqbs"
    #                     "gppqyoaoglifareljluigqyxtveukstzepridpmdltpxjmzdvatgzmqexrauywreoslyoydmiyipyqiaihfjqncelefiaxjhdaamr"
    #                     "vahbvoznsfvsdknlktsifioxjdsqldzlyzqkqxkwjfrehqbhlaanbcvxomxyypqfxbwmtaiegcjlzeslmpghirzsaprxdcbobflvbu"
    #                     "pwahxwjgrcqskewvjsjyyggozkvwwytrwpmuguclssmrshlwukkjapiwnkybydergdqkhttbakooghbskiqlesocfrjuxotecnhkf"
    #                     "mwtmzcysppmffnskvfabunfzsibqrerfstonzjhtcpnscpteflsnmqqphelpngnlnczritcjxewlhftujrpaeaxylqkswaisvzg"
    #                     "ciaemvodvcnqtuwcjkmzjzkikaqifymwwlvyxndgwwlauwiyiflgoahyaavkudvemfftzwlxdltwicouwboeaddxmvind", 22))

    str1 = "wangfei"
    ch_list = list(str1)
    print(ch_list)
    print("".join(ch_list))
    print(sp.reverseWords("Let's take LeetCode contest"))
    print(sp.checkRecord("LPLPLPLPLPL"))
