#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:qi.py
@TIME:2020/4/30 19:46
@DES: 判断某个元素是否在列表之中

'''

def solve(init_list,el):
    n = len(init_list)
    if n ==1:
        if init_list[0] == el:
            return True
        else: return  False
    left_list,right_list = init_list[:n//2],init_list[n//2:]
    res = solve(left_list,el) or solve(right_list,el)
    return res

test_list = [12,2,34,34,454,2,34,64,43]
print(solve(test_list,43))
print(solve(test_list,5))
