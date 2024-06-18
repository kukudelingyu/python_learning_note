#!/usr/bin/env python
# -*- coding: utf-8 -*-
def logging(fn):
    def inner(a, b):
        fn(a, b)
    return inner
@logging
def sum_num(a, b):
    result = a +b
    print(result)

sum_num(1, 2)
# sum_num = logging(sum_num)
# sum_num(1, 3)
