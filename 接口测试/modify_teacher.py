#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

import requests


def modify_teacher(teacherid, username, password, realname, desc, courses, display_idx, sessionid):
    teacher = {
        "action": "modify_teacher",
        "id": teacherid,
        "newdata": '''{
            "username":"%s",
        "password":"%s",
        "realname":"%s",
        "desc":"%s",
        "courses":%s,
        "display_idx":"%s"
        }''' % (username, password, realname, desc, json.dumps(courses, ensure_ascii=False), display_idx)
    }
    res = requests.put("http://localhost/api/mgr/sq_mgr/", data=teacher, cookies={"sessionid": sessionid})
    return res.json()
