#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:gui.py
@TIME:2020/4/30 19:24
@DES:阶乘
'''

def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n*jiecheng(n-1)


print(jiecheng(10))