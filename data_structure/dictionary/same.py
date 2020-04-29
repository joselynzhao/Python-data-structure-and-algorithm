#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:same.py
@TIME:2020/4/29 21:13
@DES: 获取两个字典中相同键值对的过程
'''

a = {
     'x':1,
     'y':2,
     'z':3
}
b = {
     'x':11,
     'y':2,
     'w':10
}
print(a.keys() & b.keys())  # 输出a和b中都有的key
print(a.keys() - b.keys()) # 输出a中有，但b中没有的key
print(a.items() & b.items())  # item 表示的是 key和value
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)