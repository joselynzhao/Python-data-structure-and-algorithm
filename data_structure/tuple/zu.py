#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:zu.py
@TIME:2020/4/18 21:04
@DES:创建并访问元组
'''

# 元组是用空号括起来的元素

tup1 =('google','toppr',1997,2000) #可以混杂各种类型的数据
tup2 =(1,2,3,4,5)

# 可以常见空元组
tup = ()
# 当元组中只有一个元素时，需要在元素后面添加'，'。
tup = (50,)

print(tup1[0])
print(tup2[1:5])

#google
#(2, 3, 4, 5)