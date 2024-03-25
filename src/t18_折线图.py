from pyecharts.charts import Line
from pyecharts.options import TitleOpts
from pyecharts.options import LegendOpts
from pyecharts.options import ToolboxOpts
from pyecharts.options import VisualMapOpts
import json

"""
获取美国数据
"""
# 打开文件
try:
    us_date_list = None
    us_confirm_list = None
    with open("../data/折线图数据/美国.txt", "r", encoding="utf-8") as f:
        json_string = f.read()
        response = json.loads(json_string)
        date_list = response["data"][0]["trend"]["updateDate"][:314]
        confirm_list = response["data"][0]["trend"]["list"][0]["data"][:314]
except Exception as e:
    print(f"文件打开异常：{e}")
finally:
    if date_list and confirm_list:
        line = Line()
        line.add_xaxis(date_list)
        line.add_yaxis("确诊数量", confirm_list)
        line.render()

