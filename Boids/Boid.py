# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:38:29 2020

@author: devilears
"""
import random

class Boid:
    """
    Keeps track of a Boid's position and velocity in 2 dimensions
    """
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = random.randint(1, 10)/10.0
        self.velocity_y = random.randint(1, 10)/10.0

