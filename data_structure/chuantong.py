#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:chuantong.py
@TIME:2020/4/17 21:57
@DES: 使用列表推导式
'''

#variable = [out_exp_res for out_exp in input_list if out_ex == 2]
# out_exp_res 列表生成元素表达式，可以有返回值的函数

squares = []
for x in range(10):
    squares.append(x**2) # 表示x的平方
print(squares)
squares1 = [x**2 for x in range(10)]
print(squares1)

squares2 = [x**2 for x in range(10) if x%2 is 0]
print(squares2)  #[0, 4, 16, 36, 64]

multiples = [i for i in range(30) if i%3 is 0]
print(multiples) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

