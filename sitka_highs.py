#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:14:20 2019

@author: stevenstonaker
"""

# =============================================================================
# import csv
# 
# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
# =============================================================================


# Print headers and their positions
# =============================================================================
# import csv
# 
# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
# =============================================================================


# Extracting and reading data
# =============================================================================
# import csv
# 
# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     # Get high temperatures from this file:
#     highs = [int(row[5]) for row in reader]
#     
# print(highs)
# =============================================================================


# Plotting data in a temperature chart
# =============================================================================
# import csv
# import matplotlib.pyplot as plt
# 
# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     # Get high temperatures from this file:
#     highs = [int(row[5]) for row in reader]
#     
# # Plot the high temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(highs, c='red')
# 
# # Format plot.
# plt.title("Daily high temperatures, July 2018", fontsize=24)
# plt.xlabel("", fontsize=16)
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# 
# plt.show()
# =============================================================================

# The datetime module
# =============================================================================
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
# 
# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     
#     # Get dates and high temperatures from this file:
# #    dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in reader]
# #    highs = [int(row[5]) for row in reader]
#     dates, highs = [], []
#     for row in reader:
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         high = int(row[5])
#         dates.append(current_date)
#         highs.append(high)
#     
# # Plot the high temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red')
# 
# # Format plot.
# plt.title("Daily high temperatures, July 2018", fontsize=24)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=12)
# 
# plt.show()
# =============================================================================


# Plotting a longer timeframe
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file:
#    dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in reader]
#    highs = [int(row[5]) for row in reader]
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()