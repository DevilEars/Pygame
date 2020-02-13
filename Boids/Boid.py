# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:38:29 2020

@author: devilears
"""
import math
import random

class Boid:
    """
    Keeps track of a Boid's position and velocity in 2 dimensions
    
    Boids follow three rules:
        1. Flock together towards the centre
        2. Don't bump against each other
        3. Keep up with the same velocity
    """
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = random.randint(1, 10)/10.0
        self.velocity_y = random.randint(1, 10)/10.0
        
    
    def distance(self, boid):
        """
        To determine the distance from another boid
        """
        distX = self.x - boid.x
        distY = self.y - boid.y        
        return math.sqrt(distX * distX + distY * distY)

    "Move closer to a set of boids"
    def moveCloser(self, boids):
        if len(boids) < 1: return
            
        # calculate the average distances from the other boids
        avgX = 0
        avgY = 0
        for boid in boids:
            if boid.x == self.x and boid.y == self.y:
                continue
                
            avgX += (self.x - boid.x)
            avgY += (self.y - boid.y)

        avgX /= len(boids)
        avgY /= len(boids)

        # set our velocity towards the others
        distance = math.sqrt((avgX * avgX) + (avgY * avgY)) * -1.0
       
        self.velocity_x -= (avgX / 100) 
        self.velocity_y -= (avgY / 100) 
        
    "Move with a set of boids"
    def moveWith(self, boids):
        if len(boids) < 1: return
        # calculate the average velocities of the other boids
        avgX = 0
        avgY = 0
                
        for boid in boids:
            avgX += boid.velocity_x
            avgY += boid.velocity_y

        avgX /= len(boids)
        avgY /= len(boids)

        # set our velocity towards the others
        self.velocity_x += (avgX / 40)
        self.velocity_y += (avgY / 40)
    
    "Move away from a set of boids. This avoids crowding"
    def moveAway(self, boids, minDistance):
        if len(boids) < 1: return
        
        distanceX = 0
        distanceY = 0
        numClose = 0

        for boid in boids:
            distance = self.distance(boid)
            if  distance < minDistance:
                numClose += 1
                xdiff = (self.x - boid.x) 
                ydiff = (self.y - boid.y) 
                
                if xdiff >= 0: xdiff = math.sqrt(minDistance) - xdiff
                elif xdiff < 0: xdiff = -math.sqrt(minDistance) - xdiff
                
                if ydiff >= 0: ydiff = math.sqrt(minDistance) - ydiff
                elif ydiff < 0: ydiff = -math.sqrt(minDistance) - ydiff

                distanceX += xdiff 
                distanceY += ydiff 
        
        if numClose == 0:
            return
            
        self.velocity_x -= distanceX / 5
        self.velocity_y -= distanceY / 5
        
    "Perform actual movement based on our velocity"
    def move(self):
        if abs(self.velocity_x) > maxVelocity or abs(self.velocity_y) > maxVelocity:
            scaleFactor = maxVelocity / max(abs(self.velocity_x), abs(self.velocity_y))
            self.velocity_x *= scaleFactor
            self.velocity_y *= scaleFactor
        
        self.x += self.velocity_x
        self.y += self.velocity_y

