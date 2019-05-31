#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


def delete_teacher(teacherid, sessionid):
    teacher = {
        "action": "delete_teacher",
        "id": teacherid
    }
    res = requests.delete("http://localhost/api/mgr/sq_mgr/", data=teacher, cookies={"sessionid": sessionid})
    return res.json()
