# -*- coding: utf-8 -*-
from covid19_helper.interface import *
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.options import InitOpts


# 设置html大小
def set_option(width, height):
    opt = InitOpts(
        width=width,
        height=height
    )
    return opt


# 设置map参数
def set_map(name,nums):
    # 初始化地图
    map0 = Map(
        init_opts=set_option("1200px", "600px"),
    )
    map0.add(name, data_pair=get_data_series(name), maptype="world")
    map0.set_series_opts(label_opts=opts.LabelOpts(is_show=False)).set_global_opts(
        title_opts=opts.TitleOpts(title="COVID_19 WORLD MAP"),
        visualmap_opts=opts.VisualMapOpts(max_=nums),
    )
    return map0


# 获得map
def get_map(data_set, path):
    set_map(data_set).render(path=output_path + path)
