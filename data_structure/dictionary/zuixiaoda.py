#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:zuixiaoda.py
@TIME:2020/4/30 10:32
@DES: 转换并换算数据
'''



print(sum([0,1,2]))
print(sum([0,1,2],1))

nums = [1,2,3,4,5]
s = sum(nums)
b = sum(x*x for x in nums)
print(s)
print(b)

import  os
# files = os.listdir('.idea')
# if any(name.endswith('.py') for name in files): #any 任意一个
#     print("this is a py file")
# else:
#     print("there are not py file")


s = ('RMB',40,123.4)
print(','.join(str(x) for x in s))
profolio = [
    {'name':'a','share':50},
    {'name':'b','share':34},
    {'name':'c','share':23},
    {'name':'d','share':54}
]
from operator import itemgetter
min_shares = min(profolio,key=itemgetter('share'))
min_shares = min(s['share'] for s in profolio)
print(min_shares)