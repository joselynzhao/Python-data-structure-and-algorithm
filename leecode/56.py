#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:56.py
@TIME:2020/8/2 18:40
@DES:
'''


# input = [[1, 3], [2, 6], [8, 10], [15, 18]]
# n = sorted(input)
# # print(n)
# def need_merge(input):
#     out = []
#     for i in range(len(input)):
#         out.extend(input[i])
#     sorted_out = sorted(out)
#     up = [0 if sorted_out[i+1]-sorted_out[i]>0 else 1 for i in range(len(out)-1)]
#     print(up)
#     print(sorted_out)
#     print(out)
#     if out == sorted_out and sum(up)==0:
#         return False
#     else:
#         return True
# def function(input):
#     if need_merge(input): # 需要合并
#         out = []
#         n = len(input)
#         i=0
#         while(i<n):
#             cur = input[i]
#             j = i
#             while(j<n-1 and input[j+1][0]<=cur[1]):
#                 j+=1
#             # j 是找到的最后一个起点小于cur[1]的位置
#             # 对i到j 进行合并
#             out.append([cur[0],input[j][1]]) # 如果不需要合并的话，i=j
#             i = j+1
#         print(out)
#         return function(out)
#     else:
#         return input
#
#
# # print(need_merge(input))
# print(function([[1,4],[4,5]]))

class Solution:
    def need_merge(self,intervals):
            out = []
            for i in range(len(intervals)):
                out.extend(intervals[i])
            sorted_out = sorted(out)
            up = [0 if sorted_out[i+1]-sorted_out[i]>0 else 1 for i in range(len(out)-1)]
            # print(up)
            # print(sorted_out)
            # print(out)
            if out == sorted_out and sum(up)==0:
                return False
            else:
                return True
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])  # 先按区间左边界值由小到大排序
        if self.need_merge(intervals): # 需要合并
            out = []
            n = len(intervals)
            i=0
            while(i<n):
                cur = intervals[i]
                j = i
                while(j<n-1 and intervals[j+1][0]<=cur[1]):
                    j+=1
                # j 是找到的最后一个起点小于cur[1]的位置
                # 对i到j 进行合并
                out.append([cur[0],max(intervals[j][1],cur[1])]) # 如果不需要合并的话，i=j
                i = j+1
            # print(out)
            return self.merge(out)
        else:
            return list(intervals)

# 别人的答案
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])  # 先按区间左边界值由小到大排序
        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:  # 如果结果集最后一个元素的右边界比新加入区间的左边界小，直接加入结果集
                res.append(inter)
            else:  # 否则，说明新加入的和结果集最后一个区间有重合，更新区间右边界即可
                res[-1][1] = max(res[-1][1], inter[1])
        return res

# 作者：LotusPanda
# 链接：https://leetcode-cn.com/problems/merge-intervals/solution/xiong-mao-shua-ti-python3-yi-dong-by-lotuspanda/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


