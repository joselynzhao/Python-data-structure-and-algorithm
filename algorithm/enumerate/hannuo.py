#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:hannuo.py
@TIME:2020/4/30 18:54
@DES:
'''


# 先计算需要多少步骤

def myhannou(n): # 计算步数是正确的
    if n == 1:
        return 1
    else:
        return myhannou(n-1)*2+1

print(myhannou(4))


# 考虑输出每一步的操作方法
i = 1
def move(n,nfrom,nto):
    global  i
    print("第{}步：将{}号盘子从{}移动到{}".format(i,n,nfrom,nto))
    i+=1

def hannoi(n,a,b,c): # 将第n个盘子借助b从a移动到c
    if n == 1:
        move(n,a,c)
    else:
        hannoi(n-1,a,c,b)
        move(n,a,c)
        hannoi(n-1,b,a,c)


try:
    n = int(input('n:'))
    hannoi(n,'a','b','c')
except ValueError:
    print('please input')
