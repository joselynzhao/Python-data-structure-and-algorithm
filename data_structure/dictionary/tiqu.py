#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:tiqu.py
@TIME:2020/4/29 22:35
@DES: 使用字典推导式提取字典子集
'''

prices = {
    'asp':49.9,
    'python':69.9,
    'java':59.9,
    'c':45.9,
    'php':79.9
}
p1 = {key:value for key,value in prices.items() if value>50}
print(p1)

tech_names ={'python','java','c'}

p2 = {key:value for key,value in prices.items() if key in tech_names}
print(p2)

# 相比之下后面两种方法更慢
p3 = dict((key,value) for key,value in prices.items() if value>50)
p4 = {key:prices[key] for key in prices.keys() if key in tech_names}
print(p3)
print(p4)