#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:53:25 2019

@author: stevenstonaker
"""

# =============================================================================
# import json
# 
# # Explore the structure of the data.
# filename = 'data/eq_data_1_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
#     
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)
# =============================================================================


# Make a list of all earthquakes
# =============================================================================
# import json
# 
# # Explore the structure of the data.
# filename = 'data/eq_data_1_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
#     
# all_eq_dicts = all_eq_data['features']
# 
# mags = []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     mags.append(mag)
# print(mags[:10])
# =============================================================================


# Extracting location data
import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
print(mags[:10])
print(lons[:5])
print(lats[:5])

