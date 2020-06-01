#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20060101.py
@TIME:2020/6/1 19:59
@DES: Z 字形变换
'''

import  numpy as np
s = 'LEETCODEISHIRING'
numRows = 4

len_s = len(s)
# print(len_s)
n = numRows

# 计算数组宽度
k = (n-1)*(int(len_s/(2*n-2))+1)
# print(k)

location = np.zeros([n,k],dtype = str)
# loc_len = np.zeros(n,dtype=int)
# print(loc_len)
# print(location)
arrow = 0
x,y = 0,0
for index, char in enumerate(s):
    location[x,y]=char
    # loc_len[x]=y
    if x==n-1:
        arrow=1
    if x==0:
        arrow=0
    if arrow==0: # 向下走
        x+=1
    if arrow==1: # 想上走
        x-=1
        y+=1
# print(location)
# print(loc_len)

out=''
# print(str(''.join(location)))

for i in range(n):
    out+=str(''.join(location[i,:]))

print(out)
    # for j in range(k):





