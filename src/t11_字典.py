"""
定义
{"张三":22, "李四”:25， "王五":43}

空字典
{} 或者 dict()
"""


# 字典取值
m_dict = {"张三":22, "李四":25, "王五":43}
age = m_dict["张三"]
print(f"张三的年龄为：{age}")

# 字典嵌套
m_dict = {
    "tom": {"gender": "man", "age": 22},
    "lili": {"gender": "woman", "age": 19},
    "jerry": {"gender": "man", "age": 32}
}
print(f"lili的年龄为：{m_dict["lili"]["age"]}")

# 新增元素
m_dict = {"张三": 22, "李四": 25, "王五": 43}
m_dict["zhou"] = 24
print(f"m_dict={m_dict}")

# 更新元素
m_dict = {"张三": 22, "李四": 25, "王五": 43}
m_dict["张三"] = 24
print(f"m_dict={m_dict}")

# 删除元素
m_dict = {"张三": 22, "李四": 25, "王五": 43}
m_dict.pop("张三")
print(f"m_dict={m_dict}")

# 清空元素
m_dict = {"张三": 22, "李四": 25, "王五": 43}
m_dict.clear()
print(f"m_dict={m_dict}")

# 获取全部的 key
m_dict = {"张三": 22, "李四": 25, "王五": 43}
keys = m_dict.keys()
print(f"m_dict={keys}")

# 遍历字典
for key in keys:
    print(f"key={key} value={m_dict[key]}")

for key in m_dict:
    print(key)

# len(dict) 获取字典长度
