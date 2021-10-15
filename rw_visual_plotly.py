#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:03:08 2019

@author: stevenstonaker
"""

#from plotly.graph_objs import Scatter, Layout
from plotly import offline

from random_walk import RandomWalk
    
# Make a random walk.
rw = RandomWalk(1_000)
rw.fill_walk()
point_numbers = [value for value in range(rw.num_points)]

# Visualize the results
data = [{
        'type': 'scatter',
        'x': rw.x_values,
        'y': rw.y_values,
        'mode': 'markers',
        'marker': {
                'size': 10,
                'color': point_numbers,

                'colorscale': 'Blues',
                'reversescale': True,
                'colorbar': {'title': 'Distance'},
                }
        }]

my_layout = {
        'title': f"Random Walk of {rw.num_points} points",
        }

offline.plot({'data': data, 'layout': my_layout}, filename='rw_plotly_1_000.html')