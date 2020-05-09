#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:ling.py
@TIME:2020/5/9 11:02
@DES: 解决'找零'问题
'''

def main():
    d = [0.01,0.02,0.05,0.1,0.2,0.5,1.0]
    d_num = [] # 存储每种银币的数量
    s = 0

    # 拥有零钱总和
    temp = input('请输入每种零钱的数量')
    d_num0 = temp.split()
    for i in range(0,len(d_num0)):
        d_num.append(int(d_num0[i]))
        s+=d[i]*d_num[i]
    sum = float(input("请输入需要找的零钱："))
    if sum>s:
        print("无法找零")
        return 0
    i = len(d)-1
    remain_s = sum
    while i>=0:
        k = int(remain_s/d[i])

        if k!=0:
            if k>=d_num[i]:
                k = d_num[i]
            remain_s -= k * d[i]
            print("用了{}个{:4}的银币".format(k,d[i]))
        if remain_s==0:
            break
        i -= 1


if __name__ == '__main__':
    main()

