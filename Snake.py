# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:45:46 2020

@author: devilears
"""




class Player:
    x = 5
    y = 5
    speed = 1
    
    
    # All the moves
    def moveLeft(self):
        self.x = self.x - self.speed
        
    def moveRight(self):
        self.x = self.x + self.speed

    def moveUp(self):
        self.y =  self.y - self.speed
    
    def moveDown(self):
        self.y =  self.y + self.speed