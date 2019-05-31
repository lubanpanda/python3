#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pprint

import requests


def list_course(sessionid):
    course_list = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20",
                               cookies={"sessionid": sessionid})
    pprint.pprint(course_list.json())
    return (course_list.json())
