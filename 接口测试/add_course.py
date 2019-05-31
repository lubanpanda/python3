#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


# 添加课程函数
def add_course(name, desc, display_idx, sessionid):
    course = {
        "action": "add_course",
        "data": '''{
               "name":"%s",
               "desc":"%s",
               "display_idx":"%s"
                }''' % (name, desc, display_idx)
    }
    res = requests.post("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20", data=course,
                        cookies={"sessionid": sessionid})
    return (res.json())
