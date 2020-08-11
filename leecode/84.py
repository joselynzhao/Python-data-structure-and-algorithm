#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:84.py
@TIME:2020/8/11 20:49
@DES:
'''
def get_neighbor(index):
    # index = [3,2,5,0,4,1]
    neighbor = [1]*len(index)
    for i,e in enumerate(index):
        pre = index[:i]
        cur = e
        while(cur+1 in pre):
            neighbor[i]+=1
            cur+=1
        cur = e
        while(cur-1 in pre):
            neighbor[i]+=1
            cur-=1
    return neighbor



def largestRectangleArea(heights): #超出时间限制了。
    if len(heights) == 0:
        return 0
    import numpy as np
    heights = np.array(heights)
    index = np.argsort(-heights)
    neighbor = [1] * len(index)
    for i, e in enumerate(index):
        pre = index[:i]
        cur = e
        while (cur + 1 in pre):
            neighbor[i] += 1
            cur += 1
        cur = e
        while (cur - 1 in pre):
            neighbor[i] += 1
            cur -= 1
    max = heights[index[0]]
    # print(max)
    for i,e in enumerate(index):
        cur = heights[e]*neighbor[i]
        if cur>max:
            max = cur
    return max



heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
# get_neighbor()