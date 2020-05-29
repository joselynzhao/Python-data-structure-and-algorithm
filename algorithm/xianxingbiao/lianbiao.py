#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:lianbiao.py
@TIME:2020/5/12 20:53
@DES:
'''

class Node:
    def __init__(self,data,pnext=None):
        self.data = data
        self._next=pnext

    def __repr__(self):
        return str(self.data)

