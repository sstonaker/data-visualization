#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:30:37 2019

@author: stevenstonaker
"""

import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        if column_header == 'latitude':
            index_lat = index
        if column_header == 'longitude':
            index_lon = index
        if column_header == 'bright_ti4':
            index_bright = index
        if column_header == 'acq_date':
            index_date = index

    lats, lons, brights = [], [], []
    for row in reader:
        try:
            lat = row[index_lat]
            lon = row[index_lon]
            bright = float(row[index_bright])
        except ValueError:
            print(f"Missing data for row {row}")
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)
    
# Map the fires.
data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
                'size': [bright*.015 for bright in brights],
                'color': brights,
                'line': {'width': 0},
                'colorscale': 'Reds',
                'colorbar': {'title': 'Brightness'},
                },
        }]
my_layout = Layout(title=f"World fires - last 7 days")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')