#!/usr/bin/env python
# -*- coding: utf-8 -*-
def logging(fn):
    def inner(*args, **kwargs):
        print("inner")
        fn(*args, **kwargs)
    return inner

@logging
def print_num(*args, **kwargs):
    print(args, kwargs)

print_num(1,2,3,age="18")
