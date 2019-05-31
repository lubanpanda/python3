#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


# 修改课程
def modify_course(courseid, name, desc, display_idx, sessionid):
    course = {
        "action": "modify_course",
        "id": courseid,
        "newdata": '''{
            "name":"%s",
            "desc":"%s",
            "display_idx":"%s"
        }''' % (name, desc, display_idx)
    }
    res = requests.put("http://localhost/api/mgr/sq_mgr/", data=course, cookies={"sessionid": sessionid})
    return res.json()
