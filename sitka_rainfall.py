#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:14:20 2019

@author: stevenstonaker
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and precip amounts from this file
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        precip = float(row[3])
        dates.append(current_date)
        precips.append(precip)
    
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='red')

# Format plot.
plt.title("Daily precipitation - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

# Set the y axis boundary
ax.axes.set_ybound(0, 5)

plt.show()