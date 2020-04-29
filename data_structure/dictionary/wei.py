#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:wei.py
@TIME:2020/4/29 21:21
@DES:  使用函数itemgetter()对字典进行排序
'''

from operator import itemgetter
a = [1,2,3]
b  = itemgetter(1) # 定义函数b，获取对象的第1个域的值
print(b(a))
b = itemgetter(1,0)
print(b(a))