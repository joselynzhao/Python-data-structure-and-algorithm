#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:53.py
@TIME:2020/7/30 19:06
@DES:
'''

a = [-2,1,-3,4,-1,2,1,-5,4]
a = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums) :
        n = len(nums)
        flag = [0 if nums[i] < 0 else 1 for i in range(n)]
        # print(flag,n)
        if sum(flag) == n:
            return sum(nums)
        if sum(flag) == 0:
            return max(nums)
        max_sum = nums[0]
        left, right = 0, 0
        while (right < n - 1):
            #right+=1
            while (right < n - 1 and flag[right + 1] == 0):
                right += 1 #退出时 flag[right]=0 and flag[right+1]=1
            while (right < n - 1 and flag[right + 1] == 1):
                right += 1 # when exit
            max_sum = max(max_sum, sum(nums[left:right + 1]))
            print(max_sum, left, right)
            while(left<right and flag[left+1]==1):
                left+=1
            while (left <right and flag[left+1]==0):
                left+= 1

            # left+=1
            max_sum = max(max_sum, sum(nums[left:right + 1]))
            print(max_sum, left, right)
        return max_sum
    def maxSubArray2(self, nums) :
        n = len(nums)
        flag = [0 if nums[i]<0 else 1 for i in range(n)]
        print(flag,n)
        max_sum = nums[0]
        left,right = 0,0
        while(right<len(nums)-1):
            right+=1
            while(flag[right]==0):
                right+=1
            max_sum = max(max_sum,sum(nums[left:right+1]))
            print(max_sum,left,right)
            # cur_sum =
            #             # if cur_sum>max_sum:
            #             #     max_sum = cur_sum
            left+=1
            while(flag[left]==0):
                left+=1
            max_sum = max(max_sum,sum(nums[left:right+1]))
            print(max_sum, left, right)
        return max_sum


solu = Solution()
print(solu.maxSubArray(a))
# a=[-2,1,-3,4,-1,2,1,-5,4]
# print(a[1:1])