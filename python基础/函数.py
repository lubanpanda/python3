#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# def func():#函数定义
#     print("step1")
#     print("step2")
#     print("step3")
#
# func()
# func()


# str1="name is tom tom"
# print(str1.count("tom"))

# 各个运营商的号段
# YiDong=["187","139","156"] #移动
# liantong=["135","130","177"] #联通
# dianXing=["199","133","144"] #电信
#
# tel=input("请输入需要查询的手机号：")
# if len(tel)==11:
#     if(tel.isdigit()):
#         if(tel[:3] in YiDong):
#             print("移动号段")
#         elif(tel[:3] in liantong):
#             print("联通号段")
#         elif(tel[:3] in dianXing):
#             print("电信")
#     else:
#         print("有非法字符")
# else:
#     print("手机号位数不对")


def getName(srcStr):
    return srcStr.split("the name is ")[1].split(",")[0]


print(getName('A old lady come in, the name is Mary, level 94454'))
