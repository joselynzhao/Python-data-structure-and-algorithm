#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:bahuang.py
@TIME:2020/5/9 16:07
@DES:八皇后问题
'''

n =8
x =[] # 一个解

X= [] #一组解

# 冲突检测：判断x[k]是否和前面的重复
def conflict(k):
    global x
    for i in range(k):
        if x[i] == x[k] or abs(x[i]-x[k]) == abs(i-k): # 判断是否与x[k]冲突  # 后面部分表示在对角线上
            return  True
    return False

# 套用子集树模板
def queens(k):
    global  n,x,X
    if k>=n: #超出最低行
        X.append(x[:]) # 保存（一个解），注意x[:]
    else:
        for i in range(n):
            x.append(i) # 皇后置于第i列，入栈
            if not conflict(k): # 剪枝
                queens(k+1)
            x.pop() # 回溯，出栈


def show(x):
    global  n
    for i in range(n):
        print('.'*(x[i])+'X'+'.'*(n-x[i]-1))


queens(0)
print(X[-1])
show(X[-1])
