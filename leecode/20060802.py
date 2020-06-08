#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20060802.py
@TIME:2020/6/8 21:02
@DES:三数之和
'''

def function(numbers):
    print(numbers)
    numbers.sort()
    print(numbers)


    # real = []
    # for i in numbers:
    #     if i==numbers[0]:
    #         real.append(i)
    #     elif i!=real[-1]:
    #         real.append(i)
    #     else:
    #         continue
    # numbers = real
    # print(numbers)
    k,i,j = 0,1,len(numbers)-1
    res = []
    # if len(numbers) == 3:
    #     if numbers[k]+numbers[i]+numbers[j]==0:
    #         res.append(numbers)
    #     return res
    while(k<=j-2):
        sum = numbers[k]+numbers[i]+numbers[j]
        if sum == 0:
            if [numbers[k], numbers[i], numbers[j]] not in res:
                res.append([numbers[k],numbers[i],numbers[j]])
            i+=1
            j-=1
            while (numbers[i] == numbers[i-1] and i<j): i += 1
            while (numbers[j] == numbers[j+1] and i<j): j -= 1
        elif sum>0:
            j-=1
            while (numbers[j] == numbers[j+1] and i<j): j -= 1
        elif sum<0:
            i+=1
            while (numbers[i] == numbers[i-1] and i<j): i += 1
        if j<=i:
            k+=1
            while (numbers[k] == numbers[k-1] and k<j-1): k += 1
            i = k + 1
            j = len(numbers) - 1
    print(res)

    '''运行超时了'''


numbers = [-1, 0, 1, 2, -1, -4]
function([1,2,-2,-1])