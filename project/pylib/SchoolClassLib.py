#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pprint import pprint

import requests
from cfg import g_vcode


class SchoolClassLib:
    URL = "http://ci.ytesting.com/api/3school/school_classes"

    def __init__(self):
        self.vcode = g_vcode

    # 列出班级
    def list_school_class(self, gradeid=None):
        if gradeid != None:
            params = {
                "vcode": self.vcode,
                "action": "list_classes_by_schoolgrade",
                "gradeid": int(gradeid)
            }
        else:
            params = {
                "vcode": self.vcode,
                "action": "list_classes_by_schoolgrade"
            }
        response = requests.get(self.URL, params)
        bodyDict = response.json()
        return bodyDict

    # 添加班级
    def add_school_class(self, grade, name, studentlimit):
        payload = {
            "vcode": self.vcode,
            "action": "add",
            "grade": int(grade),
            "name": name,
            "studentlimit": int(studentlimit)
        }
        response = requests.post(self.URL, data=payload)
        bodyDict = response.json()
        return bodyDict

    # 删除班级
    def delete_school_classes(self, classid):
        payload = {
            "vcode": self.vcode
        }
        url = "%s/%s" % (self.URL, classid)
        response = requests.delete(url, data=payload)
        return response.json()

    # 删除所有班级
    def delete_all_school_classes(self):
        rd = self.list_school_class()
        for one in rd['retlist']:
            self.delete_school_classes(one["id"])

        # 再列出七年级所有班级
        rd = self.list_school_class(1)
        pprint(rd, indent=2)

        if rd['retlist'] != []:
            raise Exception("cannot delete all classes")

    def classlist_should_contain(self, classlist, classname,
                                 gradename, invitecode,
                                 studentlimit, studentnumber,
                                 classid):
        item = {
            "name": classname,
            "grade__name": gradename,
            "invitecode": invitecode,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "id": classid,
            "teacherlist": []}
        print(item)
        if item not in classlist:
            raise Exception("cannot find this classlist")


if __name__ == "__main__":
    sm = SchoolClassLib()
    ret = sm.list_school_class(1)
    print(ret)
