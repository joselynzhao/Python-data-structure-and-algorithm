#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:leishili.py
@TIME:2020/4/17 21:44
@DES: 排序类定义的实例
'''

class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(19),User(17),User(18)]
print(users)

# 根据User_id排序
print(sorted(users,key=lambda u:u.user_id))
from operator import attrgetter
print(sorted(users,key = attrgetter('user_id')))
