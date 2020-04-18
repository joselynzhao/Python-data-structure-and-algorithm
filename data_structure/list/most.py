#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:most.py
@TIME:2020/4/17 21:40
@DES:
'''

words= ['look','into','my','look','into','look']

from  collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
# top_three = word_counts.items()
print(top_three)

#[('look', 3), ('into', 2), ('my', 1)]