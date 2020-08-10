#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:79.py
@TIME:2020/8/10 19:34
@DES:
'''
class Solution:
    def exist(self, board,word):
        # import numpy as np
        # board = np.array(board)
        m = len(board)
        if m == 0: return  False
        n = len(board[0])
        k = len(word)
        cur = 0
        def find_cur(i,j,cur,dic): # dic: 0 左，1 上 2， 右，3 ，下  表示上一步到这一步的移动方向。
            # 在i，j的位置上是cur。
            # 终止条件
            if cur==k-1:# 找到最后一个了。
                return True
            else:
                # 开始从四周去找下一个。
                cur+=1
                if i>0 and board[i-1][j]==word[cur] and dic!='down': #
                    out = find_cur(i-1,j,cur,'up')
                    if out == True:
                        return True
                if j>0 and board[i][j-1]==word[cur] and dic!='right':
                    out= find_cur(i,j-1,cur,'left')
                    if out == True:
                        return True
                if i<m-1 and board[i+1][j]==word[cur] and dic!='up':
                    out= find_cur(i+1,j,cur,'down')
                    if out == True:
                        return True
                if j<n-1 and board[i][j+1]==word[cur] and dic!='left':
                    out= find_cur(i,j+1,cur,'right')
                    if out == True:
                        return True
                return False
        # 双重for循环找第一个
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[cur]:
                    out = find_cur(i,j,cur,'-')
                    if out == True:
                        return True
        return False
    def exist2(self, board,word):
        # import numpy as np
        # board = np.array(board)
        m = len(board)
        if m == 0: return  False
        n = len(board[0])
        k = len(word)
        cur = 0
        def find_cur(i,j,cur,path): # dic: 0 左，1 上 2， 右，3 ，下  表示上一步到这一步的移动方向。
            # 在i，j的位置上是cur。
            # 终止条件
            if cur==k-1:# 找到最后一个了。
                return True
            else:
                # 开始从四周去找下一个。
                cur+=1
                if i>0 and board[i-1][j]==word[cur] and (i-1,j) not in path: #
                    path.append((i-1,j))
                    out = find_cur(i-1,j,cur,path)
                    if out == True:
                        return True
                if j>0 and board[i][j-1]==word[cur] and (i,j-1) not in path:
                    path.append((i , j- 1))
                    out= find_cur(i,j-1,cur,path)
                    if out == True:
                        return True
                if i<m-1 and board[i+1][j]==word[cur] and (i+1,j) not in path:
                    path.append((i + 1, j))
                    out= find_cur(i+1,j,cur,path)
                    if out == True:
                        return True
                if j<n-1 and board[i][j+1]==word[cur] and (i,j+1) not in path:
                    path.append((i, j+1))
                    out= find_cur(i,j+1,cur,path)
                    if out == True:
                        return True
                # return False
        path = []
        # 双重for循环找第一个
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[cur]:
                    path.append((i,j)) #添加元组
                    out = find_cur(i,j,cur,path)
                    if out == True:
                        return True
        return False

solu = Solution()
board =[["C","A","A"],["A","A","A"],["B","C","D"]] #目前还没有通过的用例
word = "AAB"
# board=[["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
# word="aaaaaaaaaaaaa"

print(solu.exist2(board,word))