#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:lian.py
@TIME:2020/4/18 21:08
@DES: 修改元组
'''

tup1 =('google','toppr',1997,2000) #可以混杂各种类型的数据
tup2 =(1,2,3,4,5)

# 元组一旦被创建后是不能修改的。
# tup1[0]=100  #这是非法操作

# 元组可以进行连接组合

tup3 = tup1+tup2
print(tup3)