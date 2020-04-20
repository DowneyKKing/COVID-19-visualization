# -*- coding: utf-8 -*-
from pyecharts.charts import Tab

from covid19_helper import geo
from covid19_helper.interface import *

# def main():
#     map3D.get_map("map3D.html")
#     geo.get_map("confirmed", "geo.html")
#     return True


def multiple():
    tab = Tab()
    tab.add(geo.set_map("confirmed",200000), "confirmed")
    tab.add(geo.set_map("deaths",30000), "deaths")
    tab.add(geo.set_map("recovered",90000), "recovered")
    tab.render(output_path+"tab_base.html")
    return True


if multiple():
    print("已输出html图像")





