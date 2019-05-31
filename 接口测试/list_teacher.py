#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


def list_teacher(sessionid):
    res = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20",
                       cookies={"sessionid": sessionid})
    return res.json()
