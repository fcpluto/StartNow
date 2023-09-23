#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Phil
@time: 2023/8/30 22:50
"""
#字典是无序的
# 方法一：使用lambda匿名函数取value进行排序
dict = {'a':1,'b':4,'c':2}
a1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(a1)

#### 参考代码
lst = ['a','b','a','c','a','c','b','d','e','c','a','c']
#set集合去重
cc = set(lst)
dic = {}
for e in cc:
    dic[e] = lst.count(e)
#对字典按value排序
a2 = sorted(dic.items(),key=lambda kv:kv[1],reverse=True)
print(a2)
res = []
while len(res) < 3: #前3个高频字
    for elem in a2:
        if len(res) < 3:
            res.append(elem[0])
        else:
            print(res)
print(res)


