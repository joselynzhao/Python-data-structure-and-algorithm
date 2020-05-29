#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20052901.py
@TIME:2020/5/29 19:24
@DES:3. 无重复字符的最长子串
'''

class Solution:
    def __init__(self,word):
        self.lengthOfLongestSubstring(word)
    def lengthOfLongestSubstring(self, s):
        max_len = 1
        for i in range(len(s)):
            # print(s[i])
            exsit_list = [s[i]]
            current_len = 1
            for j in range(i+1,len(s)):
                # print(s[j])
                if s[j] not in exsit_list:
                    exsit_list.append(s[j])
                    current_len +=1
                else:
                    break
            if current_len>max_len:
                max_len = current_len
        print(max_len)

s = Solution('abcabcbb')


