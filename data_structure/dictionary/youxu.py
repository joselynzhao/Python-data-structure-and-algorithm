#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:youxu.py
@TIME:2020/4/29 20:06
@DES: 使用OrderedDict创建有序字典
'''

import  collections
dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] ='v2'
dic['k3'] ='v3'
print(dic)

# dic.clear()
# print(dic)

print(dic.popitem(),dic)
print(dic.popitem(),dic)