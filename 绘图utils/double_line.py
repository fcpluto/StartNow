# encoding: utf-8
"""
@file: double_line.py
@desc:
@author: guozhen
@time: 2021/12/16
"""

import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode

x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
y_data1 = [40, 60, 22, 85, 50, 40, 35]
y_data2 = [20, 50, 12, 65, 30, 60, 65]


init_opts = opts.InitOpts(bg_color='#0e1c47')
dl = Line(init_opts=init_opts)

# 全局配置项
xaxis_opts = opts.AxisOpts(boundary_gap=False,
                           type_="category",
                           axisline_opts=opts.AxisLineOpts(is_show=True,
                                                           linestyle_opts=opts.LineStyleOpts(color='#233653')),
                           splitline_opts=opts.SplitLineOpts(is_show=True,
                                                             linestyle_opts=opts.LineStyleOpts(color='#192a44')),
                           axistick_opts=opts.AxisTickOpts(is_show=False),
                           axislabel_opts=opts.LabelOpts(is_show=True, color='#7ec7ff')
                           )
yaxis_opts = opts.AxisOpts(type_="value",
                           name="销量",
                           min_=0,
                           splitline_opts=opts.SplitLineOpts(is_show=True,
                                                             linestyle_opts=opts.LineStyleOpts(color='#192a44')),
                           axisline_opts=opts.AxisLineOpts(is_show=True,
                                                           linestyle_opts=opts.LineStyleOpts(color='#233653')),
                           axistick_opts=opts.AxisTickOpts(is_show=False),
                           axislabel_opts=opts.LabelOpts(is_show=True, color='#7ec7ff'),
                           name_textstyle_opts=opts.TextStyleOpts(color='#7ec7ff', font_size=16))
tooltip_opts = opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross')
dl.set_global_opts(xaxis_opts=xaxis_opts,
                   yaxis_opts=yaxis_opts,
                   tooltip_opts=tooltip_opts,
                   legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color='#7ec7ff')))

# 添加数据项x
dl.add_xaxis(xaxis_data=x_data)

# 添加数据项y1
dl.add_yaxis(series_name="品类 1",
             y_axis=y_data1,
             symbol='circle',
             is_symbol_show=True,
             symbol_size=5,
             is_smooth=True,
             linestyle_opts=opts.LineStyleOpts(width=5, color="rgba(25,163,223,1)"),
             itemstyle_opts=opts.ItemStyleOpts(color="rgba(25,163,223,1)", border_color="#646ace", border_width=2),
             label_opts=opts.LabelOpts(is_show=False),
             tooltip_opts=opts.TooltipOpts(is_show=True),
             areastyle_opts=opts.AreaStyleOpts(opacity=1.0, color=JsCode(
                        """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color:'rgba(25,163,223,.3)'
                            },
                            {
                                offset: 1,
                                color: 'rgba(25,163,223, 0)'
                            }
                        ])"""))
             )

dl.add_yaxis(series_name="品类 2",
             y_axis=y_data2,
             symbol='circle',
             is_symbol_show=True,
             symbol_size=5,
             is_smooth=True,
             linestyle_opts=opts.LineStyleOpts(width=5, color="rgba(10,219,250,1)"),
             itemstyle_opts=opts.ItemStyleOpts(color="rgba(10,219,250,1)", border_color="#646ace", border_width=2),
             label_opts=opts.LabelOpts(is_show=False),
             tooltip_opts=opts.TooltipOpts(is_show=True),
             areastyle_opts=opts.AreaStyleOpts(opacity=1.0, color=JsCode(
                          """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(10,219,250,.3)'
                            },
                            {
                                offset: 1,
                                color: 'rgba(10,219,250, 0)'
                            }
                        ])"""))
             )

dl.render("double_line_chart.html")
