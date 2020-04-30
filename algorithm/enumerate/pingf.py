#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:pingf.py
@TIME:2020/4/30 18:33
@DES: 计算平方根
'''

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses  = 0
ans = 0.03
high = 6.25
ans = 4.6875
low = 4.6875
while abs(ans**2-x)>=epsilon and ans<= x:
    ans+=step
    numGuesses +=1 # 枚举的次数
print('numGuesses = ',numGuesses)
print( ans)