"""
语法： 序列[起始下标:结束下标:步长] 默认可以不写

起始下标开始
结束下标处结束(不包含结束下标)
步长表示依次取元素的间隔， 负数为反向取
"""

my_list = [0, 1, 2, 3, 4, 5, 6]
result1= my_list[1:4]
print(result1)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(result2)

# 步长为负数 反向取
my_str = "0123456"
result3 = my_str[::-1]
print(f"result3的结果是{result3}")
