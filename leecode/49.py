#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:49.py
@TIME:2020/7/29 20:23
@DES:
'''


class Solution:
    def groupAnagrams(self, strs) :
        dicts = {}

        def get_dict(char):
            c = sorted(list(char))
            # c = set(c)
            return ''.join(c)

        for char in strs:
            dict = get_dict(char)
            if dict not in dicts.keys():
                dicts[dict]=[char]
            else:
                dicts[dict].append(char)

        return list(dicts.values())

solu = Solution()
out = solu.groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"])
print(out)

a0 = out
a1 = [["hos"],["boo","bob"],["nay"],["deb","deb"],["wow"],["bop"],["brr"],["hey"],["rye"],["eve"],["elf"],["pup","pup"],["bum"],["iva"],["lyx"],["yap"],["ugh","ugh"],["hem"],["rod"],["aha"],["nam"],["gap"],["yea"],["doc"],["pen"],["job"],["dis"],["max"],["oho"],["jed"],["lye"],["ram"],["qua"],["mir"],["nap"],["hog"],["let"],["gym"],["bye"],["lon"],["aft"],["eel"],["sol"],["jab"]]
a2 = [["sol"],["wow"],["gap"],["hem"],["yap"],["bum"],["ugh","ugh"],["aha"],["jab"],["eve"],["bop"],["lyx"],["jed"],["iva"],["rod"],["boo"],["brr"],["hog"],["nay"],["mir"],["deb","deb"],["aft"],["dis"],["yea"],["hos"],["rye"],["hey"],["doc"],["bob"],["eel"],["pen"],["job"],["max"],["oho"],["lye"],["ram"],["nap"],["elf"],["qua"],["pup","pup"],["let"],["gym"],["nam"],["bye"],["lon"]]

for i in a0:
    if i not in a2:
        print(i)