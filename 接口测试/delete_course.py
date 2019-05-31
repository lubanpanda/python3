#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


def delete_course(courseid, sessionid):
    course = {
        "action": "delete_course",
        "id": courseid
    }
    res = requests.delete("http://localhost/api/mgr/sq_mgr/", data=course, cookies={"sessionid": sessionid})
    return res.json()
