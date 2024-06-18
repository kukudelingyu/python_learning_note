import re

# 匹配账号，只能由字母和数字组成，长度限制6-10位
regex = "^[a-zA-Z0-9]{6,10}$"
# 匹配QQ号，纯数字，长度5-11位，开头不能是0
regex1 = "^[1-9][0-9]{4,10}"
# 匹配邮箱地址，只允许qq,163,gmail这三种邮箱格式
regex2 = "^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$"


account = input("请输入你的QQ账号：")
result = re.match(regex1, account)
if result:
    print("验证通过")
else:
    print("账号格式不正确")
