"""
True
False
==
!=
>
<
>=
<=
"""
import random

age = 30
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")

print("时间过的真快")  # 没有行首缩进不受if语句限制

if int(input("请输入你的身高(cm)：")) < 120:
    print("身高小于120cm，可以免费")
elif int(input("请输入你的VIP等级(1-5)：")) > 3:
    print("VIP等级大于3，可以免费")
elif int(input("今天是几号：")) == 1:
    print("今天是1号免费日，可以免费")
else:
    print("条件都不满足，需要买票10元")

