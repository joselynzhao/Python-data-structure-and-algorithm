#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:xian.py
@TIME:2020/5/11 21:20
@DES: 顺序存储的删除操作
'''

L  = [1,2,3,4,5,7,8]
def delete_list(L,i):
    L_length = len(L)
    if i<1 or i>L_length:
        return False
    if i<L_length:
        # del L[i]
        print(L)
        for k in range(i,L_length-1)[::1]:
            L[k]=L[k+1]
        L = L[:-1]
        print(L)

delete_list(L,3)
