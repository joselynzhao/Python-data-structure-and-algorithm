#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:qie.py
@TIME:2020/4/18 20:55
@DES: 命名切片
'''

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(items[2:4])
print(items[a])
items[a] = [10,11]  #局部替换
print(items)
print(a.start)
print(a.stop)
print(a.step)  #None
# 具有这三个属性

s = 'Helloworld'
print(a.indices(len(s)))  #将切片映射到特定大小的序列上。返回（start,stop,step）元组
for i in range(*a.indices(len(s))):
    print(s[i])

print(range(*a.indices(len(s))))



