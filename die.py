#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:46:28 2019

@author: stevenstonaker
"""

from random import randint

class Die:
    """A class representing a single die."""
    
    def __init__(self, num_sides=6):
        """"Assume a six-sided dice."""
        self.num_sides = num_sides
        
    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)