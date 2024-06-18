"""
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""

try:
    f = open("../../data/abc.txt", "r", encoding="utf-8")
except:
    f = open("../../data/abc.txt", "w", encoding="utf-8")

"""
捕获指定异常
try:
except 异常类 as e:
--------------------------------
"""

"""
捕获多个异常
try:
except (异常类, 异常类):
--------------------------------
"""

"""
try:
    do something
except:
    捕获异常
else:
    没有异常的时候会执行
finally:
    总是会执行
"""
