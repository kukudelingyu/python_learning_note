import re

# . :匹配任意一个字符（除了\n），\.匹配本身
# [] : 匹配[]中列举的字符
# \d : 匹配数字，即0-9
# \D : 匹配非数字
# \s : 匹配空白，即空格，tab键
# \S : 匹配非空白
# \w : 匹配单词字符，即a-z、A-Z、0-9、_
# \W : 匹配非单词字符

# * : 匹配前一个规则的字符出现0至无数次
# + : 匹配前一个规则的字符出现1至无数次
# ? : 匹配前一个规则的字符出现0次或1次
# {m} : 匹配前一个规则的字符出现m次
# {m,} : 匹配前一个规则的字符出现最少m次
# {m,n} : 匹配前一个规则的字符出现m到n次

# ^ : 匹配字符串开头
# $ : 匹配字符串结尾
# \b : 匹配一个单词的边界
# \B : 匹配非单词的边界

# | : 匹配左右任意一个表达式
# () : 将括号中字符作为一个分组

s = 'python itheima python2 python3'
# match 从头开始匹配 匹配第一个命中项
result = re.match('python', s)
print(result)
print(result.span())
print(result.group())
# 全局匹配， 匹配第一个命中项
result1 = re.search('python2', s)
# 全局匹配， 匹配所有命中项
result2 = re.findall('python3', s)

s1 = "itheima1 @@python2 !!666 ##itcast3"
# 找出全部的数字
result = re.findall(r'\d',s1)
print(result)
# 找出特殊字符
result1 = re.findall(r'\W', s1)
print(result1)
# 找出全部的英文字母
result2 = re.findall(r'[a-zA-Z]', s1)
print(result2)
