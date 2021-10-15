#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:30:37 2019

@author: stevenstonaker
"""

# =============================================================================
# import json
# 
# from plotly.graph_objs import Scattergeo, Layout
# from plotly import offline
# 
# # Explore the structure of the data.
# filename = 'data/eq_data_1_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
#     
# all_eq_dicts = all_eq_data['features']
# 
# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)
#     
# # Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
# my_layout = Layout(title='Global Earthquakes')
# 
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='global_earthquakes.html')
# =============================================================================


# Specify chart data with dictionary
# =============================================================================
# import json
# 
# from plotly.graph_objs import Layout
# from plotly import offline
# 
# filename = 'data/eq_data_1_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
#     
# all_eq_dicts = all_eq_data['features']
# 
# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)
#     
# # Map the earthquakes.
# data = [{
#         'type': 'scattergeo',
#         'lon': lons,
#         'lat': lats,
#         'marker': {
#                 'size': [5*mag for mag in mags],
#                 },
#         }]
# my_layout = Layout(title='Global Earthquakes')
# 
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='global_earthquakes.html')
# =============================================================================


# Customize marker color
# =============================================================================
# import json
# 
# from plotly.graph_objs import Layout
# from plotly import offline
# 
# filename = 'data/eq_data_30_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
#     
# all_eq_dicts = all_eq_data['features']
# 
# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)
#     
# # Map the earthquakes.
# data = [{
#         'type': 'scattergeo',
#         'lon': lons,
#         'lat': lats,
#         'marker': {
#                 'size': [5*mag for mag in mags],
#                 'color': mags,
#                 'colorscale': 'Viridis',
#                 'reversescale': True,
#                 'colorbar': {'title': 'Magnitude'},
#                 },
#         }]
# my_layout = Layout(title='Global Earthquakes')
# 
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='global_earthquakes.html')
# =============================================================================


# Adding hover text
import json

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/eq_data_30_day_2019_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    
all_eq_dicts = all_eq_data['features']
data_title = all_eq_data['metadata']['title']
num_events = all_eq_data['metadata']['count']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])
    
# Map the earthquakes.
data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
                'size': [5*mag for mag in mags],
                'color': mags,
                'colorscale': 'Cividis',
                'reversescale': True,
                'colorbar': {'title': 'Magnitude'},
                },
        }]
my_layout = Layout(title=f"{data_title}<br />{num_events} total events")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')