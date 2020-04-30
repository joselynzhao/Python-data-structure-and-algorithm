#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:k.py
@TIME:2020/4/30 20:16
@DES: 找出一组序列中第k小的元素
'''

'''其实相当于是一个排序问题'''

def partition(seq):
    pi = seq[0]
    lo = [x for x in seq[1:]  if x<=pi]
    hi = [x for x in seq[1:] if x>pi]
    return lo,pi,hi

def select(seq,k):
    lo,pi,hi = partition(seq)
    m = len(lo)
    if m+1 == k:
        return pi # 为什么不是lo[-1]
    elif m==k:
        return lo[-1]
    elif m<k:
        return select(hi,k-m-1)
    else:
        return select(lo,k)

seq = [3,4,1,6,3,7,9,13,93,0,100,1,2,2,3,3,2]
seq1=[1,2,3,4,5,6]
print(select(seq1,3))