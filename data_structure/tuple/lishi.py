#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:lishi.py
@TIME:2020/4/20 14:23
@DES:  历史记录统计
'''

from _collections import deque
def search(lines, pattern,history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines  #编写搜索某项记录的代码时，通常会用到含有yield关键字的生成器函数，它能够将处理搜索过程的代码和使用搜索结果的代码成功解耦开来。
        previous_lines.append(line)

# Example use on a file
if __name__ =="__main__":
    with open('123.txt') as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline)
            print(line)
            print('-'*20)
q = deque(maxlen=3)  #创建一个固定长度的队列

q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
