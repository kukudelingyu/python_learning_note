"""
集合
{1,2,3,4,5}

空集合
set()
"""

# 添加元素
m_set = {1, 2}
m_set.add(3)
print(f"m_set={m_set}")

# 移除元素
m_set = {1, 2, 3}
m_set.remove(1)
print(f"m_set={m_set}")

# 随机取出一个元素
m_set = {1, 2, 3, 4}
result = m_set.pop()
print(f"集合被取出的元素是={result}, 取出之后集合为{m_set}")

# 清空集合
m_set = {1, 2, 3, 4}
m_set.clear()
print(f"m_set={m_set}")

# 取两个集合的差集
m_set1 = {1, 2, 3, 4}
m_set2 = {1, 2, 3}
result = m_set1.difference(m_set2)
print(f"取差集后的结果为{result}，m_set1={m_set1}, m_set2={m_set2}")

# 消除差集
m_set1 = {1, 2, 3, 4}
m_set2 = {1, 2, 3}
m_set1.difference_update(m_set2)
print(f"消除差集后，m_set1={m_set1}, m_set2={m_set2}")

# 合并集合
m_set1 = {1, 2, 3}
m_set2 = {5, 6}
new_set = m_set1.union(m_set2)
print(f"两集合合并的结果为：{new_set}")

# len(set) 获取集合的长度
