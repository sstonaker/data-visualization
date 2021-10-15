#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:14:20 2019

@author: stevenstonaker
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/new_orleans_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    data_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        if column_header == 'TMAX':
            index_high = index
        if column_header == 'TMIN':
            index_low = index
        if column_header == 'NAME':
            index_name = index
        if column_header == 'DATE':
            index_date = index
        if column_header == 'PRCP':
            index_precip = index
    
    location = data_row[index_name]    
    
    # Get dates and precip amounts from this file
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[index_date], '%Y-%m-%d')        
        try:
            precip = float(row[index_precip])
        except ValueError:
            precip = 0
        else:
            dates.append(current_date)
            precips.append(precip)
    
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='red')

# Format plot.
plt.title(f"Daily precipitation - 2019\n{location}", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

# Set the y axis boundary
ax.axes.set_ybound(0, 5)

plt.show()