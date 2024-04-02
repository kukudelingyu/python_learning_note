"""
面向矿象，数据分析案网，去业务逻辑代码实现步骤：
1. 设计一个类，可以完成数据的封装
2. 设计一个抽系类，定义文件读取的相关功能，并使用子类实现具体功能
3. 渎收文件，生产数据矿象
4. 进行数据需或的逻辑计算（计算每一天的销额）
5. 通过PyEcharts进行图形绘制
"""
from pyecharts.charts import Bar
from pyecharts.options import TitleOpts

from src.数据分析案例.File_Reader import TextFileReader
from src.数据分析案例.File_Reader import JsonFileReader

text_reader = TextFileReader("../../data/2011年1月销售数据.txt")
json_reader = JsonFileReader("../../data/2011年2月销售数据JSON.txt")

text_record_list = text_reader.readFile()
json_record_list = json_reader.readFile()
all_record_list = text_record_list + json_record_list

data_dict = {}
for record in all_record_list:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money


date_list = list()
money_list = list()

for key in data_dict.keys():
    date_list.append(key)
    money_list.append(data_dict[key])

bar = Bar()
bar.set_global_opts(TitleOpts(title="1月销售额"))
bar.add_xaxis(date_list)
bar.add_yaxis("金额", money_list)
bar.render()
