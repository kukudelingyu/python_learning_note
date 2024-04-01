
# 设计一个类
class Student:
    name = None,
    age = None,
    gender = None,
    nationality = None,
    native_place = None


# 创建一个对象
stu_1 = Student()
stu_1.age = 18
stu_1.name = "张三"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东"
print(stu_1)


class Person:
    # name = None
    # age = None
    # tel = None
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def say_hello(self):
        print(f"大家好我是{self.name},我今年{self.age}岁了, 我的电话是{self.tel}")


person = Person("张三", 22, 18665666666)

person.say_hello()
