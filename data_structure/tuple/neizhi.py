#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:neizhi.py
@TIME:2020/4/18 21:15
@DES: 使用内置方法操作元组
'''

'''
元组的内置操作包含：
    len()
    max()
    min()
    tuple(seq) 列表转为元组
'''

car =['奥迪','宝马','奔驰']
print(len(car))
tup2 = (5,4,8)
tup3 = [5,4,8]
print(max(tup2)) # 字符也能求大小？
print(min(tup2))
car_tuple = tuple(tup3) # 转换为tuple
print(car_tuple)