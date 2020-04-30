#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:fen.py
@TIME:2020/4/30 09:40
@DES: 根据记录进行分组
'''

from  itertools import groupby
from operator import itemgetter

things = [('xxx',11),('xxx',3),('zzz',10),('zzz',34)]

for key,items in groupby(things,itemgetter(0)):
    print(key)
    # print(items)
    for subitem in items:
        print(subitem)

print('-'*20)


# groupby(iterable,[,key])