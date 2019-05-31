#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


def listCourse():
    params = {"action": "list_course",
              "pagenum": "1",
              "pagesize": 20}
    response = requests.get("http://localhost/api/mgr/sq_mgr/", params=params)
    return response.json()["retlist"]


if __name__ == '__main__':
    courseList = listCourse()
    for course in courseList:
        print(course)
