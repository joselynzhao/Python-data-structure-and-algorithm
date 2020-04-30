#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:hebing.py
@TIME:2020/4/30 10:50
@DES: 将多个映射合并为单个映射

'''

a = {'x':1,'z':3}
b = {'y':2,'z':4}

from collections import ChainMap
c = ChainMap(a,b)

print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
# del c['x']
print(c)
print(a)