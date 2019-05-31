#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


# 登陆
def login():
    user_info = {
        "username": "auto",
        "password": "sdfsdfsdf"
    }
    login_res = requests.post("http://localhost/api/mgr/loginReq", data=user_info)
    return login_res.json(), login_res.cookies['sessionid']
