#!/usr/bin/env python
# coding: utf-8


n = int(input())
deleted = 0

remained = list()
raw_inp = input().split(' ')
raw_inp.reverse()
for i in range(len(raw_inp)):
    num = int(raw_inp.pop())
    if (remained.count(num) == 0):
        remained.append(num)
    else:
        deleted+=1
remained.reverse()
for i in range(len(remained)):
    print(remained.pop(),end=' ')
print()
print(deleted)


# In[ ]:




