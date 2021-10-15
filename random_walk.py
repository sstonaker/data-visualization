#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:50:44 2019

@author: stevenstonaker
"""

from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            
            # Reject moves that go nowhere.
            if x_step ==0 and y_step == 0:
                continue
            
            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
    def get_step(self):
        """Calculate distance and direction of each step."""
        
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

            
class ModifiedRandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            self.get_steps()
            
            # Reject moves that go nowhere.
            if self.x_step ==0 and self.y_step == 0:
                continue
            
            # Calculate the new position.
            x = self.x_values[-1] + self.x_step
            y = self.y_values[-1] + self.y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
    def get_steps(self):
        """Determine the direction and distance for each step."""
        
        # Decide which direction to go and how far to go in that direction.
        x_direction = choice([1,])
#        x_distance = choice([0, 1, 2, 3, 4])
        x_distance = choice([0, 1, 2, 3, 4])            
        self.x_step = x_direction * x_distance
            
        y_direction = choice([1, -1])
#        y_distance = choice([0, 1, 2, 3, 4])
        y_distance = choice([0, 1, 2, 3, 4])            
        self.y_step = y_direction * y_distance
        
        