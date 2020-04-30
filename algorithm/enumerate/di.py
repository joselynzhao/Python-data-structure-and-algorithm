#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:di.py
@TIME:2020/4/30 18:44
@DES: 递归
'''
#
# fib_table = {}
# def fib_num(n):
#     if  n<=1:
#         return n
#     if n not in fib_table:
#         fib_table[n] = fib_num(n-1) +fib_num(n-2)
#
#     return fib_table[n]
#
# n = int(input("input n"))
# print(n, fib_num(n))


def myfib(n):
    if n <=2:
        return 1
    else:
        myfib(n-1)+myfib(n-2)


