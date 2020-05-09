#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:jiayou.py
@TIME:2020/5/9 11:26
@DES:  加油，使得加油次数最少
'''

def greedy():
    n = 100  # 总的储油量
    k = 5
    d = [50,80,39,60,40,32]
    # 表示加油站之间的距离
    num = 0
    # 表示加油的次数
    for i in range(k):
        if d[i]>n:
            print('no solution') # 应该是大于油仓量
            return
    i, s = 0,0
    while i<=k:
        s +=d[i]
        if s>=n:
            # 当局部和大于n时，将局部和更新为当前距离
            s = d[i]
            # 贪心在于让每一次加满油之后跑尽可能远的距离
            num+=1
        i +=1
    print(num)

if __name__ =='__main__':
    greedy()


    ''' 这个算法还不是很清楚'''

