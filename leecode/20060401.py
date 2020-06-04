#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20060401.py
@TIME:2020/6/4 20:48
@DES: 回文数 : 已解除，但时间超出限制，需要动态规划

'''


def longestPalindrome( s: str) -> str:
    # 先考虑极端情况
    lens = len(s)
    if lens == 1:
        return s[0]
    if lens == 0:
        return ''
    if lens == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    max_len, max_char = 1, s[0]
    for i in range(lens - 1):
        for j in range(i+2, lens+1):
            curr_s = s[i:j]
            if len(curr_s) == 2:
                if curr_s[0] == curr_s[1]:
                    if max_len < 2:
                        max_len = 2
                        max_char = curr_s
            else:
                huiwen = ishuiwen(curr_s)
                if huiwen == 0:
                    continue
                elif huiwen == -1:
                    return "huiwen==-1,error"
                else:
                    if huiwen > max_len:
                        max_len = huiwen
                        max_char = curr_s
    return max_char


def ishuiwen(s):
    lens = len(s)
    if lens >= 2:
        for i in range(int(lens / 2)):
            if s[i] == s[lens - 1 - i]:
                continue
            else:
                return 0  # 不是回文数
        return lens
    return -1  # error


print(longestPalindrome("abb"))