
class Student:

    # 私有成员变量
    __money = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # toString 方法
    def __str__(self):
        return f"我是{self.name},我今年{self.age}岁了"

    # 小于或大于方法
    def __lt__(self, other):
        return self.age < other.age

    # 小于等于或者大于等于方法
    def __le__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    # 私有方法
    def __shopping(self):
        self.__money -= 10

    def tuixiao(self):
        self.__shopping()

    def getMoneyCount(self):
        return self.__money


stu1 = Student("张三", 18)
stu2 = Student("李四", 28)
# print(stu1)
# print(stu1 > stu2)
stu2.tuixiao()
print(stu2.getMoneyCount())

