#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20060801.py
@TIME:2020/6/8 20:25
@DES:11. 盛最多水的容器
'''


def maxArea(height):
    '''暴力循环'''
    # max = 0
    # # print(index)
    # for i in range(len(height)):
    #     for j in range(i,len(height)):
    #         area = min(height[i],height[j])*abs(i-j)
    #         if area>max:
    #             max = area
    # print(max)
    '''双指针'''
    i,j = 0,len(height)-1
    max = 0
    while(i!=j):
        # 计算当前面积
        area = min(height[j],height[i])*(j-i) # j-i非负
        if area>max:
            max = area
        if height[i]>=height[j]:
            j-=1
        else:
            i+=1
    print(max)











maxArea([1,8,6,2,5,4,8,3,7])