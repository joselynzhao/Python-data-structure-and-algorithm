#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:pai.py
@TIME:2020/4/29 21:24
@DES: 使用itemgetter 排序字典
'''

from operator import itemgetter
rows = [
    {'fname':'aaa','lname':'zhao','uid':1001},
    {'fname':'bbb','lname':'zhou','uid':1002},
    {'fname':'ccc','lname':'wu','uid':1004},
    {'fname':'ddd','lname':'li','uid':1003}
]

rows_by_fname = sorted(rows,key = itemgetter('fname'))
rows_by_uid = sorted(rows,key = itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

rows_by_fname = sorted(rows,key = itemgetter('lname','fname'))
print(rows_by_fname)

rows_by_fname = sorted(rows,key = lambda r:r['fname'])
print(rows_by_fname)

print(min(rows,key = itemgetter('uid')))