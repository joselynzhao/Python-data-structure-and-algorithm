#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:shan.py
@TIME:2020/4/18 21:11
@DES: 删除元组
'''

# 可以删除整个元组 del语句
tup1 =('google','toppr',1997,2000) #可以混杂各种类型的数据

print(tup1)
del tup1
try:
    print(tup1)
except NameError:
    print("错误啦")
