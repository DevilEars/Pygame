# -*- coding: utf-8 -*-
"""
This is the board for the snake

This only checks for collisions

@author: devilears
"""

class Board:
    '''
    The environment physics and other constraints are maintained here
    '''
    board_x = 800
    board_y = 600
    
    def __init__(self, x, y):
        self.board_x = x
        self.board_y = y
        
    def isCollision(self, x1, y1, x2, y2, bsize):
        '''
        checks whether the point x1 y1
        overlaps with x2 y2 plus the size
        '''
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
    
    def isPointOutsideBoard(self, x1, y1):
        '''
        checks whether the given point is outside of the board
        '''
        if x1 < 0 or x1 > self.board_x or y1 < 0 or y1 > self.board_y:
            return True
        return False