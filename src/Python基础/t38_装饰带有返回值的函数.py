#!/usr/bin/env python
# -*- coding: utf-8 -*-
def logging(fn):
    def inner(a, b):
        return fn(a, b)
    return inner
@logging
def sum_num(a, b):
    result = a +b
    return result

res = sum_num(4, 2)
print(res)
# sum_num = logging(sum_num)
# sum_num(1, 3)
