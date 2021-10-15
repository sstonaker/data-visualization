#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:47:46 2019

@author: stevenstonaker
"""
import matplotlib.pyplot as plt


from die import Die

die = Die(6)
rolls = 10_000

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(rolls)]
    
# Analyze the results.
max_result = die.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
x_values = list(range(2, max_result+1))

# Plot the points in the walk.
plt.style.use('classic')

# Adjust the plot to fit the screen using figsize.
fig, ax = plt.subplots(figsize=(18,9))
ax.bar(x_values, frequencies)

title= f"{rolls} D{max_result} rolls"
plt.title(title, fontsize=20)
plt.xlabel('Value', fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()