#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 不带参数的get请求
import requests

res = requests.get("http://www.cnblogs.com/yoyoketang/")
print(res.status_code)

print(res.headers)

print(res.text)
