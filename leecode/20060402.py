#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:20060402.py
@TIME:2020/6/4 21:17
@DES:7. 整数反转
'''
'''简单粗暴的错误方法'''

# def reverse(self, x: int) -> int:
#     n = x
#     listn = []
#     while (n != 0):
#         k = n % 10
#         n = n / 10
#         listn.append(k)
#     lenl = len(listn)
#     sum = 0
#     for i in range(lenl):
#         sum += listn[i] * pow(10, lenl - 1 - i)
#     if x <= 0:
#         sum = -sum
#     return sum

# x = -123
#
# print(bin(x))
# n = bin(x)
# print(n)
# print(type(n))
# start_point = 2
# qianzui = '0b'
# if n[0]=='-':
#     start_point=3
#     qianzui='-0b'
# real_n = list(map(int,n[start_point:]))
# print(real_n)
# for i in range(len(real_n)):
#     real_n[i]=1-real_n[i]
#
# print(real_n)
#
# out = qianzui+''.join(map(str,real_n))
# print(out)
#
# print(int(out,2))


x = 1563847412
fuhao = 0
if x<0:
    x = -x
    fuhao=-1

xx = list(str(x))
xxx = list(map(int,xx))
print(xxx)

sum = 0
lens = len(xxx)
for i in range(lens):
    current = xxx[i]*pow(10, i)
    sum += current
print(sum)

if sum>pow(2,32):
    print(0)

if fuhao==-1:
    sum=-sum
print(sum)

print(pow(2,31))
