#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:youxianpy.py
@TIME:2020/4/25 20:22
@DES:
'''

'''
使用内置模块heapq可以实现一个简单的优先级队列。
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
q = PriorityQueue()
q.push(Item('A'),1) #数字越小优先级越高
q.push(Item('B'),4)
q.push(Item('C'),5)
q.push(Item('D'),1)
print(q.pop())  #第一次执行pop()操作返回的元素具有最高的优先级。相同优先级顺序同插入时相同。
print(q.pop())
print(q.pop())

