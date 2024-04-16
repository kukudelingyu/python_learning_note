from pyspark import SparkContext, SparkConf
import os

"""
单词计数统计
"""
os.environ["PYSPARK_PYTHON"] = "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12"

# 1. 创建SparkContext 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_count")
sc = SparkContext(conf=conf)

# 2. 读取文件
rdd = sc.textFile("../data/word.txt")
list_out = rdd.collect()
# 3. 将元素当做key，默认value为1
count_map = {}
# 4. 每重复一次 value+1
for ele in list_out:
    list_in = ele.split(" ")
    for ele_in in list_in:
        if ele_in in count_map.keys():
            count_map[ele_in] += 1
        else:
            count_map[ele_in] = 1

keys_list = count_map.keys()
# 5. value就是每个单词出现的次数
for ele in keys_list:
    print(f"{ele}---:{count_map[ele]}")
sc.stop()

