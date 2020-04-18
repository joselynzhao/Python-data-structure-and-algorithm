#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:buhaxi.py.py
@TIME:2020/4/17 21:18
@DES:  针对不是散列的情况下 ，删除重复元素
'''

def buha(items,key = None):
    seen =  set()
    for item in items:
        val = item if key is None else key(item) #!!! key的功能是将序列中的元素转化为可散列的类型。这样方便检测重复
        if val not in seen:
            yield item
            seen.add(val)

    print(seen) # set([(10, 15), (2, 3), (1, 4)])

if __name__ == '__main__':
    a = [
        {'x':2,'y':3},
        {'x':1,'y':4},
        {'x':2,'y':3},
        {'x':2,'y':3},
        {'x':10,'y':15}
    ]
    print(a)
    print(list(buha(a,key = lambda b:(b['x'],b['y']))))  #!!!

    # [{'y': 3, 'x': 2}, {'y': 4, 'x': 1}, {'y': 15, 'x': 10}]

    a = [5, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    print(list(buha(a)))  #[5, 2, 1, 9, 10]
