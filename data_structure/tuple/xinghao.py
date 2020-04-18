#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:xinghao.py
@TIME:2020/4/18 21:22
@DES: 将序列分解为单独的变量
'''

p = (4,5)
x,y = p
print(x)
print(y)
print(x,y) #这样输出的是一个元组吗？

data = ['acme',60,91,(12,12,23)]
a,b,c,d = data
print a
print b
print c
print(d)

'''
也就是说，元组和列表都可以通过这种形式进行分解'''

# 星号表达式
records = [
    ('aaa',1,2),
    ('bbb','hello'),
    ('ccc',5,3)
]
def do_foo(x,y):
    print('AAA',x,y)
def do_bar(s):
    print('BBB',s)
for tag,*args in records:  # python3 支持
    if tag =='AAA':
        do_foo(*args)
    elif tag=='BBB':
        do_bar(*args)

line = 'guan:ijing234://wef:234:guan'
print(len(line.split(':')))
uname,*fields,homedir,sh = line.split(':')
print(uname,fields,homedir,sh)

