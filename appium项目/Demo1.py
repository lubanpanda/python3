#!/usr/bin/env python3
# -*- coding:utf-8 -*-

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.1',
    'deviceName': 'test',
    'app': r'D:\多多计算器.apk',
    'appPackage': 'com.ibox.calculators',  # app包名
    'appActivity': 'com.ibox.calculators.SplashActivity',
    'unicodeKeyboard': True,  # 指定输入法
    'noReset': True,
    'newCommandTimeout': 6000,
    'automationName': 'uiautomator2'
}
