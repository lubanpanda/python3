#!/usr/bin/env python3
# -*- coding:utf-8 -*-

name = "tom"
age = 20
# info="名字是：%s,年龄是：%10d"%(name,age)
# info1="名字是：%s,年龄是：%-10d"%(name,age)#有-号左对齐
# print(info1)
# 顺序填坑
# info="名字是：{}，年龄是：{}".format(name,age)
# print(info)

# 用下标填坑
info = "名字是：{0}，年龄是：{1}".format(name, age)
print(info)

# 用变量填坑
info = "名字是：{name}，年龄是：{age}".format(name=name, age=age)
print(info)

# 指定长度
info = "名字是：{:0>6}，年龄是：{:0>6}".format(name, age)  # 首选 >大于号 ---右边，<  小于号----左边， ^ 异或 ---中间
print(info)
