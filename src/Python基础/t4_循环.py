import random

num = random.randint(1, 100)
print(f"随机数是{num}")
count = 0
flag = True

while flag:
    guess_num = int(input("请输入猜测的数字"))
    count += 1
    if guess_num == num:
        print("恭喜你猜中了")
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")

print(f"你总共猜了{count}次")

# 定义字符串
name = "duanlingyu"
# for 循环
for x in name:
    print(x)

# range(num) 获取一个从0开始到num结束的数字序列，不含num
list1 = range(5)
for x in list1:
    print(x)
# range(num1,num2) 获取一个从num1开始到num2结束的数字序列，不含num2
list2 = range(5, 10)
for x in list2:
    print(x)
# range(num1,num2,step) 获取一个从num1开始到num2结束的数字序列，不含num2, 数字步长为step
list3 = range(1, 20, 3)
for x in list3:
    print(x)

# continue 和 break 进行循环的跳过和中断
