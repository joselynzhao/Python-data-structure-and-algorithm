#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:xiu.py
@TIME:2020/4/29 19:56
@DES: 修改字典
'''


dict = {'shuxue':99,'yuwen':99,'yingyu':99}
print('shuxue:',dict['shuxue'])
print('yuwen:',dict['yuwen'])
print('yingyu:',dict['yingyu'])
dict['wuli'] = 100
dict['huaxue'] = 89
print(dict)

dict['yuwen'] = 80
print(dict['yuwen'])