#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. 定义一个file类
class File(object):
    def __init__(self, file_name, file_model):
        self.file_name = file_name
        self.file_model = file_model

    def __enter__(self):
        print("这是上文")
        self.file = open(self.file_name, self.file_model)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("这是下文")
        self.file.close()


with File("../../data/abc.txt", "r") as f:
    file_data = f.read()
    print(file_data)

