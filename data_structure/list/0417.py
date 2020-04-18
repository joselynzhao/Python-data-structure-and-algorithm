#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:0417.py
@TIME:2020/4/17 20:44
@DES: 实现可散列情况下的删除重复元素功能
'''
car = ['hhh','bom']
print(car)

numbers = list(range(1,4))   # 左臂右开
print(numbers)  #[1, 2, 3]

print(car[0])

# 通过title()获取一盒列表元素
print(car[0].title())
print('dabda'[1])

def dedupe(items):
    seen = set()  # 字典？
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    print(seen)

if __name__=='__main__':
    a = [5,5,2,1,9,1,5,10]
    print(a)
    print(list(dedupe(a)))


