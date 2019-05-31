#!/usr/bin/env python3
# -*- coding:utf-8 -*-
fileDir = "D:/学习笔记/test.txt"
file_object = open(fileDir, "r", encoding="utf-8")  # r----字符串：txt log    b---二进制
print(file_object)
print(file_object.tell())  # 获取文件指针
print(file_object.read(2))
print(file_object.tell())

# o模式，从0开始，配套"r"   1模式：当前位置 配套"rb" 读二进制  2模式：尾部位置 配套"rb"
file_object.seek(1, 0)
# 文件里面的换行/r/n

print(file_object.readline())  # --返回的是str
print(file_object.readlines())  # 返回的是列表
print(file_object.read().splitlines())  # 返回的是去换行符的列表

fo = open(fileDir, "w")
fo.write("123344")
fo.write("34444")
fo.flush()
fo.close()
