name = "张三"
age = 19
salary = 892.53

# print("我的名字是:"+name+"我的年龄是:"+age) 字符串不能通过“+”拼接别的类型
print("我的名字是:%s，年龄是:%d，工资是:%f" % (name, age, salary))
print(f"我的名字是:{name}，年龄是:{age}，工资是:{salary}")

'''
可以使用m.n精度控制
m 控制宽度，要求是数字，小于本身宽度不生效
.n 控制小数精度，要求是数字，会进行四舍五入
'''
print("我的名字是:%s，年龄是:%5d，工资是:%.5f" % (name, age, salary))