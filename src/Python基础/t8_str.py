# 同元组一样，字符串也是一个无法修改的容器

my_str = "GOSKI APP"

value = my_str[2]
print(value)

# 通过下标获取索引
value1 = my_str[-1]
print(value1)

# index
value2 = my_str.index("O")
print(value2)

# replace 方法
new_my_str = my_str.replace("G", "A")
print(new_my_str)

# split 方法
my_str_list = my_str.split(" ")
print(my_str_list)

# strip 方法, str.strip()去除首尾空格，str.strip(元素)去除首尾元素(匹配所有字符)
my_str = "12GOSKI APP21"
new_str = my_str.strip("12")
print(new_str)

# count 方法
value4 = my_str.count("G")
print(value4)

# len(str) 获取字符串的长度
