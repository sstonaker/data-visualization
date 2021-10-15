#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:25:33 2019

@author: stevenstonaker
"""

# =============================================================================
# # First 5 cube numbers.
# import matplotlib.pyplot as plt
# 
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]
# 
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values)
# 
# # Set chart title and label axes.
# ax.set_title('Cube Numbers', fontsize=24)
# ax.set_xlabel('Value')
# ax.set_ylabel('Cube of Value')
# 
# # Set size of tick labels
# ax.tick_params(axis='both', which='major')
# 
# plt.show()
# =============================================================================


#First 5000 cube numbers
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes.
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value')
ax.set_ylabel('Cube of Value')

# Set size of tick labels
ax.tick_params(axis='both', which='major')

# Set the range for the axes.
ax.axis([0, 5100, 0, 5100**3])

plt.show()