#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:shaixuan.py
@TIME:2020/4/17 22:04
@DES:
'''

mylist = [1,4,-5,10,-7,2,3,-1]
# zheng
zheng = [n for n in mylist if n>0]
print(zheng)
fu = [n for n in mylist if n<0]
print(fu)