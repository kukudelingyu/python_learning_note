#!/usr/bin/env python
# -*- coding: utf-8 -*-

# _call_方法 一个类里面一旦实现了_call_方法，那么这个类创建的对象就是一个可调用对象，可以像函数一样调用

class Check(object):
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print("登录")
        self.fn()

# c = Check()
# c()

@Check
def comment():
    print("发表评论")

comment()
