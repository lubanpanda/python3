#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests


def function():
    s = 'https://www.meishij.net/'
    a = requests.get(s, params={
        'name': 'panda'
    })
    print(a.text)


# if __name__ == '__main__':
#   cc=1
#  print(cc)
# function()

c = 123456
print('第一种%s' % c)
print(f'{c}')
