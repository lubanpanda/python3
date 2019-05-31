#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import sys

from list_course import list_course
from login import login
from modify_course import modify_course

# 登录
print("开始登录")
log_res = login()[0]
if log_res['retcode'] == 0:
    print("登陆成功")
else:
    print("登陆失败")
sessionid = login()[1]

# 显示课程列表
course_list = list_course(sessionid)['retlist']
courelength = len(course_list)  # 的课程数

# 修改课程
if courelength <= 0:
    print("课程数为0，无法进行修改操作")
    sys.exit()
else:
    print("开始修改课程")
    random_index = random.randint(0, len(course_list) - 1)
    print(random_index)
    course_id = course_list[random_index]['id']  # 随机课程的id
    suffix = str(random.randint(0, 99999999))
    res_modify = modify_course(course_id, "物理" + suffix, "初中物理", '4', sessionid)
    print(res_modify)
    assert res_modify["retcode"] == 0

    course_list = list_course(sessionid)['retlist']
    for course in course_list:
        if course['id'] == course_id:
            assert course['display_idx'] == 4
            assert course['name'] == '物理' + suffix
            assert course['desc'] == '初中物理'
            print("修改成功")
