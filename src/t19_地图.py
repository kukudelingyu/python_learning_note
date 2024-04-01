import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts
from pyecharts.options import VisualMapOpts

try:
    with open("../data/地图数据/疫情.txt", "r", encoding= "utf-8") as f:
        json_str = f.read()
        province_list = json.loads(json_str)["areaTree"][0]["children"]
        data = []
        for ele in province_list:
            province_name = ele["name"] + "省"
            province_confirm_count = ele["total"]["confirm"]
            data.append((province_name, province_confirm_count))
        print(data)
        confirm_map = Map()
        confirm_map.add("各省份确诊人数", data, "china")
        confirm_map.set_global_opts(
            title_opts=(TitleOpts(title="全国疫情分布图")),
            visualmap_opts=VisualMapOpts(
                is_show=True,
                is_piecewise=True,
                pieces=[
                    {"min":1, "max":99, "lable":"1-99人", "color":"#CCFFFF"},
                    {"min":100, "max":999, "lable":"100-999人", "color":"#FFFF99"},
                    {"min":1000, "max":9999, "lable":"1000-9999人", "color":"#FF9966"},
                    {"min":10000, "max":99999, "lable":"10000-99999人", "color":"#FF6666"},
                    {"min":100000, "lable":"100000+", "color":"#CC3333"},
                ]
            )
        )
        confirm_map.render("全国疫情.html")
except Exception as e:
    print(f"文件打开异常{e}")
finally:
    print("结束")
