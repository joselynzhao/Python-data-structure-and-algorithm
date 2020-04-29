#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:jisuan.py
@TIME:2020/4/29 20:58
@DES: 对字典做计算
'''

price= {
    'xiaomi':899,
    'huawei':1999,
    'sanxing':5999,
    'guge':4999
}
k = zip(price.values(),price.keys())
print(k)
min_price = min(zip(price.values(),price.keys()))
print(min_price)
print(k)
max_price = max(zip(price.values(),price.keys()))
print(max_price)
price_sorted = sorted(zip(price.values(),price.keys()))
print(price_sorted)
price_and_name = zip(price.values(),price.keys())  # zip()创建的迭代器，内容只能被消费一次。
# print(min(price_and_name))
print(min(price))
print(max(price))

print(min(price.values()))
print(max(price.values()))
print(min(price,key=lambda k:price[k]))
print(max(price,key=lambda k:price[k]))