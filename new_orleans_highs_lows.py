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
    
    location = data_row[index_name]
    
    # Get dates and high and low temperatures from this file:
    dates, highs, lows = [], [], []
    
    for row in reader:
        current_date = datetime.strptime(row[index_date], '%Y-%m-%d')
        try:
            high = int(row[index_high])
            low = int(row[index_low])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title= f"Daily high and low temperatures - 2019\n{location}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

# Set the range for the axes.
ax.axes.set_ybound(0, 130)

plt.show()