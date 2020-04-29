#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:zitui.py
@TIME:2020/4/29 22:22
@DES: 使用字典推导式
'''

mcase = {'a':10,'b':24,'A':7,'Z':3}
mcase_frequency = {
    k.lower():mcase.get(k.lower(),0)+mcase.get(k.upper(),0) # lower和upper分别为转化为小写和大写
    # .get(key, default_value) 根据键获取值，若键不存在，则返回默认值
    for k in mcase.keys()
    if k.lower() in ['a','b']
}
print(mcase_frequency) #{'a': 17, 'b': 24}
print([k.lower() for k in mcase.keys()]) # ['a', 'b', 'a', 'z'] b的lower（）还是b

# 快速更快key和value的值
mcase_frequency = {v:k for k,v in mcase.items()}
print(mcase_frequency)