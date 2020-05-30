#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20053001.py
@TIME:2020/5/30 18:38
@DES:
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # print(len(nums1),len(nums2))
        if len(nums2)!=0:
            for one in nums2:
                nums1.append(one)
        nums1.sort()
        out= 0
        flag = int(len(nums1)/2)
        if (len(nums1)%2==0):#偶数
            out = (nums1[flag]+nums1[flag-1])/2.0
        else:
            out = float(nums1[flag])
        return out