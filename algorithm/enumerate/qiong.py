#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:qiong.py
@TIME:2020/4/30 18:21
@DES:
'''

# from  import itera
import itertools

def twentifour(cards):
    '''历史上最短计算24点的代码'''
    for nums in itertools.permutations(cards): # 四个数
        for ops in itertools.product('+-*/',repeat=3): # 三个运算符（可以重复）
            # 构造三种中缀表达式（bsd）
            pass


        '''不明白这三种中缀表达式是如何构造出来的'''
