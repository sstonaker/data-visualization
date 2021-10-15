#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:30:40 2019

@author: stevenstonaker
"""

import matplotlib.pyplot as plt

from random_walk import ModifiedRandomWalk
    
# Make a random walk.
rw = ModifiedRandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')

# Adjust the plot to fit the screen using figsize.
fig, ax = plt.subplots(figsize=(18,9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Emphasize the first and last points
ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
           s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()