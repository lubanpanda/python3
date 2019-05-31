#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 带参数的get请求
import requests

url = "http://zzk.cnblogs.com/s/blogpost/"
par = {"Keywords": "yoyoketang"}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Cookie": "_ga=GA1.2.762348983.1542767857; __gads=ID=c34a6b03fea363db:T=1542767857:S=ALNI_MauNZQnXpcnA3-hqjShZpwO1QkRhg; DetectCookieSupport=OK; .AspNetCore.Session=CfDJ8KlpyPucjmhMuZTmH8oiYTOiImz%2BVq3DxeexII%2Fb27e%2Bi7BiE8G4ZO9Z3Wo5JiR1SxgrctkHK7gaauEAh5vM6q7FPTZn7Pg6qwgTK1uBHw07yPvt9Ppe7uKGSs%2FoBGy723qhFwH1UHYE9lAL8kAnqsajty9Iep%2Fgqff946Y8hhCo; ZzkNoRobotCookie=CfDJ8KlpyPucjmhMuZTmH8oiYTPDpuiqUsVS-97ellTzmkYNmnws6eYkVt2uWEKcDKrctv4uyEuT2jiHBF9NxoM_8nwUe5E8hB2eHXSTp1HzqvQ7i7X8nKbH-y0yQE_TE6NICQ"}
res1 = requests.get(url=url, params=par, headers=header)
print(res1.status_code)
print(res1.url)
