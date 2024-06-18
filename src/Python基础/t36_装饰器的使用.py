#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import time
# 1.定义装饰器
def get_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print(f'时间：{end-start}')
    return inner

# 需要被装饰的函数
@get_time
def func():
    for i in range(10000):
        print(i)

func()
