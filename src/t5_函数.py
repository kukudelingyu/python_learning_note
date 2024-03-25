"""
def 函数名(参数):
    函数体
    return 返回值
"""


# 定义一个函数，完成相加功能
def add_count(a, b):
    return a + b


# 函数的返回值，通过变量去接收
num = add_count(1, 2)
print(num)


# None <class NoneType>

"""
函数的多种传参
"""


# 位置参数
def user_info(name, age, gender):
    print(f"你的名字是：{name}，你的年龄是：{age}，你的性别是：{gender}")


user_info("张三", 23,"女")

# 关键字参数
user_info(gender="男", name="小明", age=12)


# 缺省参数
def user_info1(name, age=12, gender="男"):
    print(f"你的名字是：{name}，你的年龄是：{age}，你的性别是：{gender}")


user_info1("小天")


# 位置不定长，传递进所有的参数都会被args变量手机，它会根据传进参数的位置合并为一个元组（tuple），args是元组类型
def user_info2(*args):
    print(args)


# 关键字不定长，参数值是“键=值”的形式的情况下，所有的键值对都会被kwargs接收，同时会根据键值对组成字典
def user_info3(**kwargs):
    print(kwargs)

user_info3(name="tom", age=32, gender="男")

# 匿名函数
def test_fun(compute):
    result = compute(1, 2)
    print(result)

test_fun(lambda x,y: x+ y)
