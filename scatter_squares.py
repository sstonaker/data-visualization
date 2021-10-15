#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:10:57 2019

@author: stevenstonaker
"""

# =============================================================================
# import matplotlib.pyplot as plt
# 
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
# 
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)
# 
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# 
# # Set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)
# 
# # Set the range for each axis.
# ax.axis([0, 1100, 0, 1100000])
# plt.show()
# =============================================================================


# =============================================================================
# # Use color as tuple.
# import matplotlib.pyplot as plt
# 
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
# 
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=(0, .8, 0), s=10)
# 
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# 
# # Set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)
# 
# # Set the range for each axis.
# ax.axis([0, 1100, 0, 1100000])
# plt.show()
# =============================================================================

# Use a colormap
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])
plt.show()

# Save the figure automatically
plt.savefig('squares_plot.png', bbox_inches='tight')