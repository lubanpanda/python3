#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import sys

from delete_course import delete_course
from list_course import list_course
from login import login

# 登录
print("开始登录")
log_res = login()[0]
if log_res['retcode'] == 0:
    print("登陆成功")
else:
    print("登陆失败")
sessionid = login()[1]

# 显示删除前的课程列表
courseListBef = list_course(sessionid)['retlist']
courseCountBef = len(courseListBef)  # 删除前的课程数
print(courseCountBef)

# 开始删除课程
if courseCountBef <= 0:
    print("课程列表中无课程")
    sys.exit()
else:
    print("开始删除课程")
    random_index = random.randint(0, courseCountBef - 1)  # 随机生成删除的课程的序列号
    course_id = courseListBef[random_index]['id']  # 随机课程的id
    res_delete = delete_course(course_id, sessionid)
    assert res_delete["retcode"] == 0

    # 显示删除后的课程列表
    courseListAft = list_course(sessionid)['retlist']
    courseCountAft = len(courseListAft)  # 删除后的课程数
    print(courseCountAft)
    assert courseCountBef - courseCountAft == 1
    for course in courseListAft:
        assert course['id'] != course_id
    print("删除成功")
