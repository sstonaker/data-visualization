#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:03:08 2019

@author: stevenstonaker
"""

# =============================================================================
# import matplotlib.pyplot as plt
# 
# from random_walk import RandomWalk
#     
# # Make a random walk.
# rw = RandomWalk()
# rw.fill_walk()
# 
# # Plot the points in the walk.
# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
#     
# plt.show()
# =============================================================================


# =============================================================================
# # Customize the plot
# import matplotlib.pyplot as plt
# 
# from random_walk import RandomWalk
#  
# # Keep making new walks, as long as the program is active.
# while True:
#     
#     # Make a random walk.
#     rw = RandomWalk()
#     rw.fill_walk()
# 
#     # Plot the points in the walk.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_values, rw.y_values, s=15)
#     
#     plt.show()
#     
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == 'n':
#         break
# =============================================================================


# =============================================================================
# # Color the points
# import matplotlib.pyplot as plt
# 
# from random_walk import RandomWalk
#     
# # Make a random walk.
# rw = RandomWalk()
# rw.fill_walk()
# 
# # Plot the points in the walk.
# plt.style.use('classic')
# fig, ax = plt.subplots()
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#            edgecolors='none', s=15)
#     
# plt.show()
# =============================================================================


# =============================================================================
# # Emphasize the first and last points
# import matplotlib.pyplot as plt
# 
# from random_walk import RandomWalk
#     
# # Make a random walk.
# rw = RandomWalk()
# rw.fill_walk()
# 
# # Plot the points in the walk.
# plt.style.use('classic')
# fig, ax = plt.subplots()
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#            edgecolors='none', s=15)
# 
# # Emphasize the first and last points
# ax.scatter(0,0, c='green', edgecolors='none', s=100)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
#            s=100)
#     
# plt.show()
# =============================================================================


# =============================================================================
# # Clean up the axes.
# import matplotlib.pyplot as plt
# 
# from random_walk import RandomWalk
#     
# # Make a random walk.
# rw = RandomWalk()
# rw.fill_walk()
# 
# # Plot the points in the walk.
# plt.style.use('classic')
# fig, ax = plt.subplots()
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#            edgecolors='none', s=15)
# 
# # Emphasize the first and last points
# ax.scatter(0,0, c='green', edgecolors='none', s=100)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
#            s=100)
# 
# # Remove the axes.
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
# 
# plt.show()
# =============================================================================


# Adding plot points.
import matplotlib.pyplot as plt

from random_walk import RandomWalk
    
# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')

# Adjust the plot to fit the screen using figsize.
fig, ax = plt.subplots(figsize=(18,9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=15)

# Emphasize the first and last points
ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
           s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()