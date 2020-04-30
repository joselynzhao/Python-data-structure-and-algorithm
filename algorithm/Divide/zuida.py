#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:zuida.py
@TIME:2020/4/30 19:31
@DES: 求顺序表中的最大值
'''

def get_max(max_list):
    if len(max_list)==2:
        return max(max_list[0],max_list[1])
    else:
        return max_list[0]


def get_max_list(init_list):
    n = len(init_list)
    if n<=2:
        return get_max(init_list)
    left_list,right_list = init_list[:n//2],init_list[n//2:]  #" // "表示整数除法。
    left_max,right_max = get_max_list(left_list),get_max_list(right_list)
    return get_max([left_max,right_max]) # 组合为list再传进去


test_list = [12,2,34,34,454,2,34,64,43]
print(get_max_list(test_list))
