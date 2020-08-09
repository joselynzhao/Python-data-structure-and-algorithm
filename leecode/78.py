#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:78.py
@TIME:2020/8/9 19:58
@DES:
'''


class Solution:
    def subsets(self, nums):
        # 先从小到大排序
        # nums.sort()
        # print(nums)
        cur = []
        res = []
        res.append(cur)
        # print(res)

        def find(cur, f):
            # 递归一次 f+1
            if f == len(nums):
                return
            if f == 0:
                for i in nums:
                    curr=cur+[i]
                    res.append(curr)
                    find(curr, f + 1)
            else:
                for i in nums:
                    if i > cur[-1]:
                        curr=cur+[i]
                        # print(curr)
                        res.append(curr)
                        # print(res)
                        find(curr, f + 1)

        find(cur,0)
        return res
nums=[1,2,3]
solu = Solution()
print(solu.subsets(nums))

