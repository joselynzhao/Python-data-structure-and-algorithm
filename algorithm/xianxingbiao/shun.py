#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:shun.py
@TIME:2020/5/11 21:41
@DES: 顺序表的插入、检索、删除和反转操作
'''

class SeqList(object):
    def __init__(self,max=8):
        self.max = max
        self.num = 0
        self.date = [None] * self.max
    def is_empty(self):
        return self.num is 0
    def is_full(self):
        return  self.num is self.max

    def __getitem__(self,key):
        if not isinstance(key,int): #判断是不是这个类型
            raise TypeError
        if 0<=key < self.num:
            return self.date[key]
        else:
            return IndexError
    def __setitem__(self, key, value):
        if not isinstance(key,int):
            raise TypeError
        if 0<=key <self.num:
            self.date[key] = value
        else:
            raise IndexError

