"""
列表
[元素1, 元素2, 元素3]

空列表
[] 或者 list()

嵌套列表
[[1,2,3], [4,5,6]]

元素类型不受限
["a", 11, True]
"""


# 列表[下标索引], 从前往后是0，1，2...  从后往前是-1，-2，-3...
name_list = ["tom", "lili", "weifang"]
print(name_list[0])
print(name_list[-1])


# 嵌套列表
num_list = [[1, 2, 3], [4, 5, 6]]
print(name_list[0][1])

"""
list.index(元素) 获取元素对应的下标
list[下标] = 新元素  修改对应下标的值
list.insert(下标，元素)  在对应下标插入元素
list.append(元素)  在list末尾追加一个元素
list.extend(元素容器)   在list末尾追加一批元素
del list[下标]    删除对应下标的元素
list.pop(2) 删除对应下标的元素，并返回
list.remove(元素) 删除列表中的第一个匹配元素
list.clear() 清空列表
list.count(元素)  返回列表中元素的数量
len(list) 返回列表的元素数量
"""
