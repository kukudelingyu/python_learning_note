from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("spark_test")
context = SparkContext(conf=conf)
print(context.version)
context.stop()
