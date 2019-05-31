#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#  ==值相等  is 值相等，而且地址也相等
[-5, 256]
a = 257
b = 257
print(a is b)

# 不相等 ！=
# print("abcd">"b")
# in 和 not in
str1 = "name is tom"
print("tom" in str1)

alist = [1, 2, 3, [10, 11]]
print(10 in alist)
print(1 in alist)

score = int(input("请输入分数"))

if score >= 90:  # --往后缩进tab  --往前缩进tab+shift
    print("A等级")
elif score >= 80:
    print("B等级")
elif score >= 70:
    print("C等级")
elif score >= 60:
    print("D等级")
else:
    print("不及格")
print("game over")
