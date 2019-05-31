#!/usr/bin/env python3
# -*- coding:utf-8 -*-
with open("bs1.html", encoding="utf-8") as f:
    html_doc = f.read()
# 导入Beautifulsoup
from bs4 import BeautifulSoup

# 指定用Html5lib解析html_doc
soup = BeautifulSoup(html_doc, "html5lib")

print(soup.find("title"))
print(soup.title.string)
print(soup.title.get_text())

print(soup.div["id"])  # 获取元素属性
