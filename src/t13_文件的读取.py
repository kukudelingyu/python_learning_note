"""
打开文件
open(name, mode, encoding)
name: 文件名
mode: 只读、写入、追加(r, w, a)
encoding: 编码格式，如UTF-8

f = open(name=test.txt, mode="r", encoding="utf-8")

读取文件
read(num) num不传表示读取全部文件
readline() 读取一行
readlines() 读取整个文件，返回一个列表，每一行的数据为一个元素

"""


# f = open("../data/fileLearning.txt", "r", encoding="utf-8")
# result = f.read()
# print(result)
# f.close()

# with open 语法操作, 不需要调用close，会自动关闭
# with open("../data/fileLearning.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)

# 写文件
with open("../data/fileLearning1.txt", "w", encoding="utf-8") as f:
    f.write("GOSKI APP升级公告")
    # f.flush()
    f.close() # close自带flush

