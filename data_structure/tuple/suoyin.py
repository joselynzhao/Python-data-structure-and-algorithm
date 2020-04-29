#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:suoyin.py
@TIME:2020/4/29 19:46
@DES: 优先级队列
'''

import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item)) # 插入
        self._index +=1
    def pop(self):
        return  heapq.heappop(self._queue)[-1] #移除

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self): # 默认情况下，__repr__() 会返回和调用者有关的 “类名+object at+内存地址”信息
        return 'Item({!r})'.format(self.name)


a = Item('a')
b = Item('b')
a = (1,Item('a'))
b = (5,Item('b'))
print(a<b)
c = (1,Item('c'))
a = (1,0,Item('a'))
b = (5,1,Item('b'))
c = (1,2,Item('c'))
print(a<b)
print(a<c)