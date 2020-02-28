# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:48:37 2020

After my Snake app, a Board to control the GoF environment

@author: devilears
"""

class Board:
    """
    The environment physics and other constraints are maintained here
    """
    
    boardWidth = boardHeight = 10
    
    
    def __init__(self, cells):
        self.boardHeight = cells
        self.boardWidth = cells
