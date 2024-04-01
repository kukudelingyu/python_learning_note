from pyecharts.charts import Line
from pyecharts.options import TitleOpts
from pyecharts.options import LegendOpts
from pyecharts.options import ToolboxOpts
from pyecharts.options import VisualMapOpts
from pyecharts.options import LabelOpts
import json

"""
获取美国数据
"""
# 打开文件
try:
    us_date_list = None
    us_confirm_list = None

    jp_date_list = None
    jp_confirm_list = None

    in_date_list = None
    in_confirm_list = None
    with open("../data/折线图数据/美国.txt", "r", encoding="utf-8") as f:
        us_json_string = f.read()
        response = json.loads(us_json_string)
        us_date_list = response["data"][0]["trend"]["updateDate"][:314]
        us_confirm_list = response["data"][0]["trend"]["list"][0]["data"][:314]

    with open("../data/折线图数据/日本.txt", "r", encoding="utf-8") as f:
        jp_json_string = f.read()
        response = json.loads(jp_json_string)
        jp_date_list = response["data"][0]["trend"]["updateDate"][:314]
        jp_confirm_list = response["data"][0]["trend"]["list"][0]["data"][:314]

    with open("../data/折线图数据/印度.txt", "r", encoding="utf-8") as f:
        in_json_string = f.read()
        response = json.loads(in_json_string)
        in_date_list = response["data"][0]["trend"]["updateDate"][:314]
        in_confirm_list = response["data"][0]["trend"]["list"][0]["data"][:314]
except Exception as e:
    print(f"文件打开异常：{e}")
finally:
    line = Line()
    line.set_global_opts(
        title_opts=TitleOpts(title="2020年美国、日本、印度新冠确诊人数", pos_left= "center", pos_bottom="1%"),
    )
    if us_date_list and us_confirm_list:
        line.add_xaxis(us_date_list)
        line.add_yaxis("美国确诊数量", us_confirm_list, label_opts=LabelOpts(is_show=False))

    if jp_date_list and jp_confirm_list:
        line.add_yaxis("日本确诊数量", jp_confirm_list, label_opts=LabelOpts(is_show=False))

    if in_date_list and in_confirm_list:
        line.add_yaxis("印度确诊数量", in_confirm_list, label_opts=LabelOpts(is_show=False))
        line.render()

