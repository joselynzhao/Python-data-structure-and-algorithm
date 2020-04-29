#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:yingshe.py
@TIME:2020/4/29 19:58
@DES: 映射多个值
'''

# d = {
#     'a':[1,2,3],
#     'b':[4,5]
# }
# e = {
#     'a':{1,2,3},
#     'b':{4,5}
# }
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d)
d = defaultdict(set)
d['a'].add(1)  # 集合中添加新元素要用add
d['a'].add(2)
d['a'].add(3)
print(d)
d ={}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('a',[]).append(3)
print(d)
d = {}
for key, value in d:
    if key not in d:
        d[key] =[]
    d[key].append(value)
d = defaultdict(list)
print(d)
for key,value in d:
    d[key].append(value)
print(d)
