#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append(r"D:\python项目\python基础")
from phone.apple import iphone6, iphone7
from phone.samsung.note import galaxy_note8
from phone.samsung.s import galaxy_s7

iphone6.askPrice()
iphone7.askPrice()
galaxy_note8.askPrice()
galaxy_s7.askPrice()
