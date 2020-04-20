# -*- coding: utf-8 -*-
from covid19_helper.interface import *
import pyecharts.options as opts
from pyecharts.charts import MapGlobe
from pyecharts.faker import POPULATION
from pyecharts.options import TooltipOpts


def set_map():
    map0 = (
        MapGlobe().add(
            maptype="world",
            series_name="World Population",
            data_pair=get_data_series("confirmed"),
            is_map_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    map0.set_series_opts(label_opts=opts.LabelOpts(is_show=False)).set_global_opts(
        title_opts=opts.TitleOpts(title="COVID_19 WORLD MAP"),
        visualmap_opts=opts.VisualMapOpts(max_=800000))
    return map0


def get_map(path):
    set_map().render(path=output_path + path)



