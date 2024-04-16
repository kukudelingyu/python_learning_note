import os
from pyspark import SparkConf, SparkContext


os.environ["PYSPARK_PYTHON"] = "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_add")
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize({1,2,3,4,5})
rdd4 = sc.parallelize({"key1":"value1","key2":"value2"})
rdd5 = sc.textFile("../../data/abc.txt")

# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())

def func(data):
    return data * 10

rdd_r1 = rdd1.map(func)
print(rdd_r1.collect())

rdd_r2 = rdd_r1.map(lambda x:x+5)
print(rdd_r2.collect())
