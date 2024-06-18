#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2024/6/18
# 1.定义一个装饰器（装饰器的本质是闭包）
def check(fn):
    def inner():
        print('登录验证')
        fn()
    return inner
@check
def comment():
    print('发表评论')

# comment = check(comment)
# comment()

comment()
