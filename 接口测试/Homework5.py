#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pprint
import random

import requests


# 登陆
def login():
    user_info = {
        "username": "auto",
        "password": "sdfsdfsdf"
    }
    login_res = requests.post("http://localhost/api/mgr/loginReq", data=user_info)
    return login_res.json(), login_res.cookies['sessionid']


'''data格式传递'''


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


# 列出课程函数
def list_course(sessionid):
    course_list = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20",
                               cookies={"sessionid": sessionid})
    return (course_list.json())


print("开始登录")
res_login = login()[0]
sessionid = login()[1]
if res_login['retcode'] == 0:
    print("登陆成功")
else:
    print("登陆失败")

print("开始添加课程")
course_name = "初中化学q" + str(random.randint(0, 9999999))  # 随机生成课程名，保证不同名
res_json = add_course(course_name, "初中化课程", "3", sessionid)
# 判断返回结果是否为0
print(res_json)
assert res_json["retcode"] == 0  # 判断返回结果是否为0
courseId = res_json["id"]  # 获取返回的课程Id
course_list = list_course(sessionid)["retlist"]  # 获取课程列表
pprint.pprint(course_list)
course = {
    "id": courseId,
    "name": course_name,
    "desc": "初中化课程",
    "display_idx": 3
}
if course_list.count(course) == 1:
    print("添加成功")
elif course_list.count(course) == 0:
    print("添加失败")
elif course_list.count(course) >= 2:
    print("添加了多个课程")
#
#
# #json格式传递
# # course={
# #  "action":"add_course_json",
# #    "data":{
# #                    "name":"初中化学222s2",
# #                    "desc":"初中化学课程",
# #                    "display_idx":"3"
# #                     }
# #         }
# # res=requests.post("http://localhost/apijson/mgr/sq_mgr/",json=course)
# print(res.json())

sessionid = login()[1]
