#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:fenzu.py
@TIME:2020/4/30 09:48
@DES: 使用groupby实现负责分组
'''

rows = [
    {'address':'xxx','data':'1111'},
    {'address':'yyy','data':'1112'},
    {'address':'zzz','data':'1113'},
    {'address':'aaa','data':'1111'},
    {'address':'bbb','data':'1112'},
    {'address':'ccc','data':'1113'}
]

from itertools import groupby
from operator import  itemgetter
rows.sort(key = itemgetter('data'))
for data, items in groupby(rows,key=itemgetter('data')):
    print(data)
    for i in items:
        print(' ',i)
#
#
from collections import  defaultdict

rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['data']].append(row)
for r in rows_by_date['1113']:
    print(r)
