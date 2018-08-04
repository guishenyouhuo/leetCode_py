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
    测试
"""
sp = StringProblems()
print(sp.reverseStr("uxzpsogzkwgwacxxvvzlhkaahjaqagdfjkmyutvhxclzskvxckjvfgzptlzldjwhrpocfugzqkpaxexezbvggtkoxriysqivup"
                    "ofrcoxbrdgccvphvdtvrjtsbospmgyfduvaslnvxwuepleziodaaqmonsxjszyjwjmvgdqgowjjtwdmynvirnlujimedfyntgacn"
                    "tvyqujvehhvruiolfkeprqpzdvmapeukemmzxdtyolxeixatgsupvpidmeyifjyxkzudxvsunghtklzgxsjhrxgxgqcdebukrarpk"
                    "pqmusempvulagashxpaisfvetrmiqiordsyjgyjmkvavxorrmnxbiikuxmezpkhgkjzmapldnmjvfxtmckskiwhdnuqpqrsrdspxuix"
                    "xnibjxoyagijmlbhjtuchzbdpaxommfvlbpxfnzkkcdentdhhxracunvrtqxrbqanufaglncjqiwofanuznfmbtjalehlqidtcmqbs"
                    "gppqyoaoglifareljluigqyxtveukstzepridpmdltpxjmzdvatgzmqexrauywreoslyoydmiyipyqiaihfjqncelefiaxjhdaamr"
                    "vahbvoznsfvsdknlktsifioxjdsqldzlyzqkqxkwjfrehqbhlaanbcvxomxyypqfxbwmtaiegcjlzeslmpghirzsaprxdcbobflvbu"
                    "pwahxwjgrcqskewvjsjyyggozkvwwytrwpmuguclssmrshlwukkjapiwnkybydergdqkhttbakooghbskiqlesocfrjuxotecnhkf"
                    "mwtmzcysppmffnskvfabunfzsibqrerfstonzjhtcpnscpteflsnmqqphelpngnlnczritcjxewlhftujrpaeaxylqkswaisvzg"
                    "ciaemvodvcnqtuwcjkmzjzkikaqifymwwlvyxndgwwlauwiyiflgoahyaavkudvemfftzwlxdltwicouwboeaddxmvind", 22))