#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20060501.py
@TIME:2020/6/5 18:46
@DES: 8. 字符串转换整数 (atoi)
'''
#
# s = '     23'
# # s = '23'
# # s='   -42'
# s="4193 with words"
# s="words and 987"
# s="-91283472332"
# k = int(s)
# s = '-'
# print(k)
# print(s)

'''这种思路不对'''
# def myAtoi(self, s: str) -> int:
#     s = s.split(' ')
#     # print(s)
#     for sp in s:
#         if sp == '':
#             continue
#         if sp[0] in list(map(str, range(1, 10))):
#             if '.' in sp:
#                 sp = min(round(float(sp)), pow(2, 31) - 1)
#             else:
#                 sp = min(int(sp), pow(2, 31) - 1)
#             return sp
#         elif sp[0] == '-' and len(sp) != 1:
#             if sp[1] in list(map(str, range(1, 10))):
#                 if '.' in sp:
#                     sp = max(round(float(sp)), -pow(2, 31))
#                 else:
#                     sp = max(int(sp), -pow(2, 31))
#                 return sp
#         else:
#             return 0
#     return 0


# s = '2234eweqqe'
# out=''
number  = list(map(str,range(1,10)))
# start = -1
# end = -1
# flag = 'sea'
# for index,ss in enumerate(s):
#     if start==-1:
#     # print(index,ss)
#         if ss==' ':
#             continue
#         elif ss not in number and ss not in ['+','-']:
#             print(0)
#             break
#     elif ss in number:
#         if start ==-1:
#             start = index
#             end = index+1 #取开区间
#             if index!=0 and s[index-1]=='-':
#                 start = index-1
#         else:
#             end = index+1
#
# print(s[start:end])
# start = -1
# end = -1
# s = "+-2"
# for index,ss in enumerate(s):
#     if ss==' ':
#         continue
#     elif ss not in number and ss not in ['+','-']:
#         break
#     else:
#         start = index
#         end = index+1
#         break
# if start!=-1:
#     if len(s)-start<=1 and s[start] in ['+','-']:
#         print(0)
#     for i in range(start+1,len(s)):
#         if s[i] in number:
#             end = i+1
#         else:
#             break
# else:
#     print(0)
#
# print(s[start:end])

def myAtoi(s: str) -> int:
    # s = '+-2'
    start = -1
    end = -1
    number = list(map(str, range(0, 10)))
    # number = ['1','2','3','4','5','6','7','8','9']
    if s=='' or s==' ':
        return 0
    for index, ss in enumerate(s):
        if ss == ' ':
            continue
        elif ss not in number and ss not in ['+', '-']:
            return  0
        elif ss in ['+','-']:
            if index!=len(s)-1: # 不是最后一位
                if s[index+1] not in number:
                    #后面不是数字
                    return  0
                else:
                    start = index
                    end = index+1
                    break
            else:
                return  0
        else:
            start=index
            end = index+1
            break
    if start ==-1:
        return 0
    for i in range(start + 1, len(s)):
        if s[i] in number:
            end = i + 1
        else:
            break
    out = int(s[start:end])
    if out>0:
        out = min(out,pow(2,31)-1)
    else:
        out = max(out,-pow(2,31))
    return out


print(myAtoi('  '))




