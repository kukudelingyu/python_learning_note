
class Phone:
    IMEI = None
    producer = "小米"

    def call_by_4g(self):
        print("使用4g通话")


class RemoteControl:
    producer = "海信"

    def control_tv(self):
        print("控制电视")


class Phone2024(Phone, RemoteControl):
    face_id = None

    def call_by_5g(self):
        print("使用5g通话")


# phone = Phone2024()
# phone.call_by_4g()
# phone.control_tv()

# 多继承中，同名属性先继承优先
# print(phone.producer)


# pass关键字 用来补全语法
class Phone2025(Phone2024):
    producer = "苹果"

    def call(self):
        pass


# 在子类中调用父类成员
class MyPhone(Phone2025):

    def call(self):
        # 父类名.成员 调用，
        print(Phone2025.producer)
        Phone2024.call_by_5g(self)
        # super().成员 调用
        super().call_by_4g()


phone = MyPhone()
phone.call()
