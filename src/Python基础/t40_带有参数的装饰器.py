#!/usr/bin/env python
# -*- coding: utf-8 -*-
def logging(flag):
    def decorator(fn):
        def inner(a, b):
            if flag == "+":
                print("--正在努力加法计算--")
            elif flag == "-":
                print("--正在努力减法计算--")
            result = fn(a, b)
            print(f"结果为：{result}")
        return inner

    return decorator

@logging('+')
def add(a, b):
    result = a+b
    return result

add(3,4)
