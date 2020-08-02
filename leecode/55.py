#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:55.py
@TIME:2020/8/1 18:44
@DES:
'''

# 时间超出限制了
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums)==1:
#             return True
#         flag = [1 if len(nums) - 1 - i <= nums[i] else 0 for i in range(len(nums) - 1)]
#         # 先考虑递归终止条件
#         if sum(flag)==0:
#             return False
#         if flag[0]==1:
#             return True
#         # 进入子问题
#         for i in range(len(flag)):
#             if flag[i]==1:
#                 return self.canJump(nums[:i+1])

# 超时
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums)==1:
#             return True
#         flag = [1 if len(nums) - 1 - i <= nums[i] else 0 for i in range(len(nums) - 1)]
#         # 先考虑递归终止条件
#         if sum(flag)==0:
#             return False
#         if flag[0]==1:
#             return True
#         # 对flag进行修整，避免重复计算。
#         for i in range(len(flag)):
#             if flag[i] == 1:
#                 # print(flag[i + 1:min(i + nums[i] + 1, len(nums))])
#                 is_jump = sum(flag[i + 1:min(i + nums[i] + 1, len(nums))]) > 0
#                 if is_jump:  # 可达范围内有可达
#                     flag[i] = 0
#         # 进入子问题
#         for i in range(len(flag)):
#             if flag[i]==1:
#                 return self.canJump(nums[:i+1])

def canJump( nums) :
        if len(nums)==1:
            return True
        flag = [1 if len(nums) - 1 - i <= nums[i] else 0 for i in range(len(nums) - 1)]
        # 先考虑递归终止条件
        if sum(flag)==0:
            return False
        if flag[0]==1:
            return True
        # 进入子问题
        is_out = 0
        for i in range(len(flag)-1,0,-1):
            if is_out:
                break
            if flag[i]==1:
                is_out = 1
                return canJump(nums[:i+1])
        # return  False

# 别人的答案
class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i



new_nums = [2,3,1,1,4]
c = canJump(new_nums)
print(c)



