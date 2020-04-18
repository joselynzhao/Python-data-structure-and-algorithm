#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:yield.py
@TIME:2020/4/17 21:11
@DES:
'''

def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)

print(list(foo(0)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

