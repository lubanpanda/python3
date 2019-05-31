#!/usr/bin/env python3
# -*- coding:utf-8 -*-
alist=[1,5,0,9,2]
for i in range(len(alist)-1):
    for j in range(len(alist)-i-1):
        if(alist[j]>alist[j+1]):
            alist[j],alist[j+1]=alist[j+1],alist[j]
print(alist  )