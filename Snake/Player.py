# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:50 2020

@author: devilears
"""

class Player:
    '''
    Keeps track of the player's snake. This means maintaining position on the
    board, as well as the length based on how many apples have been eaten
    
    Moves are also controlled here, as the player's position and direction and
    length are all contained here
    
    The board keeps track of colissions in the environment
    '''
    x = [0]
    y = [0]
    step = 20# might be too big for my 10x10 sprites
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*self.step
       self.x[2] = 2*self.step
 
    def update(self):
 
        '''
        updates the position of the the player
        '''
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            # up to one minus length, as the snake moves
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            # one step size at a time
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    
    # $$$$$$ Moves like jaguar snake $$$$$$
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    # $$$$$$ Renders player's snake $$$$$$
    # don't play with your snake in public
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 