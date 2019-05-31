#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 添加同名老师
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

from add_course import add_course
from add_teacher import add_teacher
from list_course import list_course
from list_teacher import list_teacher
from login import login

# 登录
print("开始登录")
log_res = login()[0]
if log_res['retcode'] == 0:
    print("登陆成功")
else:
    print("登陆失败")
sessionid = login()[1]

# 添加课程
print("开始添加课程")
course_name = "初中化学q" + str(random.randint(0, 9999999))  # 随机生成课程名，保证不同名
res_json = add_course(course_name, "初中化课程", "3", sessionid)
# 判断返回结果是否为0
print(res_json)
assert res_json["retcode"] == 0  # 判断返回结果是否为0
courseId = res_json["id"]  # 获取返回的课程Id
course_list = list_course(sessionid)["retlist"]  # 获取课程列表
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

# 第一次添加老师
print("开始第一次添加老师")
username = "zyz_" + str(random.randint(0, 9999999))  # 用户名
print(username)
resAddTeacher = add_teacher(username, "123444", "朱元璋", "朱元璋老师", [{"id": courseId, "name": course_name}], 1,
                            sessionid)  # 添加老师
# 判断是否添加成功
assert resAddTeacher["retcode"] == 0
teacherId = resAddTeacher["id"]  # 获取添加的教师id
teachers = list_teacher(sessionid)['retlist']  # 教师列表
teachersLengthBef = len(teachers)  # 第一次添加后的老师数量
teacher = {
    "username": username,
    "realname": "朱元璋",
    "display_idx": 1,
    "courses": [{"course_id": courseId}],
    "id": teacherId,
    "desc": "朱元璋老师"
}
print(teacher)
if teachers.count(teacher) == 1:
    print("添加老师成功")
else:
    print("添加老师失败")

# 第二次添加老师
resAddTeacher_2 = add_teacher(username, "123444", "朱元璋", "朱元璋老师", [{"id": courseId, "name": course_name}], 1,
                              sessionid)  # 添加老师
print(resAddTeacher_2)
assert resAddTeacher_2["retcode"] == 1
assert resAddTeacher_2["reason"] == "登录名 " + username + " 已经存在"
teachersLengthAf = len(list_teacher(sessionid)["retlist"])
assert teachersLengthAf - teachersLengthBef == 0
print("用例通过")
