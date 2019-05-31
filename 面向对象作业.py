#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from random import randint
from time import time


class Tiger:  # 老虎类
    className = "Tiger"

    def __init__(self, weight=200):
        self.weight = weight

    def tell_weight(self):
        print("体重：", self.weight)

    def roar(self):  # 叫唤
        self.weight -= 5
        print("wow")

    def feed(self, food):  # 喂食
        if (food == "meat"):
            print("喂食正确，体重增加10斤")
            self.weight += 10
        elif (food == "grass"):
            print("喂食错误，体重减少10斤")
            self.weight -= 10


class Sheep:
    className = "Sheep"

    def __init__(self, weight=200):
        self.weight = weight

    def tell_weight(self):
        print("体重：", self.weight)

    def roar(self):  # 叫唤
        self.weight -= 5
        print("mie~")

    def feed(self, food):  # 喂食
        if (food == "grass"):
            print("喂食正确，体重增加10斤")
            self.weight += 10
        elif (food == "meat"):
            print("喂食错误，体重减少10斤")
            self.weight -= 10


class Room:
    def __init__(self, num, animal):
        self.num = num
        self.animal = animal


# 随机生成房间，并放入动物
room_list = []
for i in range(1, 11):
    ran = randint(0, 1)
    if (ran == 0):
        room = Room(i, Tiger())
    else:
        room = Room(i, Sheep())
    room_list.append(room)

start_time = time()  # 游戏开始计时
while True:
    current_time = time()  # 当前时间
    if (current_time - start_time >= 180):  # 判断游戏是否开始了3分钟
        for room in room_list:  # 打印游戏结束后的房间及动物西信息
            print("房间号为:%s,动物是：%s,体重为:%s" % (room.num, room.animal.className, room.animal.weight))
        break
    else:
        ran = randint(1, 10)
        choose = input("当前房间为%s,请选择敲门还是喂食? 敲门输入Y，喂食输入N。" % ran)  # 判断是喂食还是敲门
        if (choose.strip() == "Y"):  # 敲门
            room_list[ran - 1].animal.roar()
        food = input("请输入meat或grass进行喂食:")  # 直接喂食，判断喂草还是肉
        room_list[ran - 1].animal.feed(food.strip())
