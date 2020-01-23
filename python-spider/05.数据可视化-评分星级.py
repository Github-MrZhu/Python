#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from pyecharts import Pie

#  获取评论中所有评分
rates = []
with open('comments.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        rates.append(row.split(',')[4])

# print(rates)

# 定义星级
attr = ['五星', '四星', '三星', '二星', '一星']
value = [
    rates.count('5') + rates.count('4.5'),
    rates.count('4') + rates.count('3.5'),
    rates.count('3') + rates.count('2.5'),
    rates.count('2') + rates.count('1.5'),
    rates.count('1') + rates.count('0.5')
]
# print(value)

pie = Pie("《一出好戏》评分星级", title_pos='center', width=900)
pie.add("", attr, value, is_label_show=True, is_legend_show=False)
pie.render('电影评分-饼图.html')
