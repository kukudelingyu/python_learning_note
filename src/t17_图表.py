# pyecharts.org
# gallery.pyecharts.org

from pyecharts.charts import Line
from pyecharts.options import TitleOpts
from pyecharts.options import LegendOpts
from pyecharts.options import ToolboxOpts
from pyecharts.options import VisualMapOpts

# 得到折线图对象
line = Line()
# 全局配置
line.set_global_opts(
    title_opts= TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts= LegendOpts(is_show=True),
    toolbox_opts= ToolboxOpts(is_show=True),
    visualmap_opts= VisualMapOpts(is_show=True)
)
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加Y轴数据
line.add_yaxis("GDP", ["100", "190", "60"])
# 将代码生成为图像
line.render()
