#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:cha.py
@TIME:2020/5/11 21:03
@DES:
'''

def insert_list(L,i,element):
    L_length = len(L)
    if  i< 1 or i>L_length: # 我感觉应该允许L_length加1
            return  False
    if i <= L_length: # 全部往后移
        for k in range(i-1,L_length)[::-1]: # 这个地方看不懂 # 这个的意思是倒着
            print(k)
            x = [L[k]]
            print(x)
            # L[k+1] = L[k]
            L[k+1:k+2] = [L[k]]
        L[i-1] = element
    print(L)
    return True

L = [1,2,3,4]
insert_list(L,2,0)

L[2:3] =[L[0]]
print(L)