# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:21:40 2020

@author: devilears
"""

import pygame
from pygame.locals import QUIT

import time

class BoidsApp:
    """
    Classic Boids
    """
    maxVelocity = 10
    numBoids = 50
    boids = []
        
    
    
    def __init__(self):
        self.caption = 'Boids'
        
        
    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        
        # surfaces, to give the boids a texture maybe

        
        # start running the game!
        self._running = True

    
    def on_event(self, event):
        # Esc key to exit
        if event.type == QUIT:
          self._running = False    

    
    # these method names are taken from 
    # pseudo code of Reynold's original boids algorithm
    # they can be named better, but I kept the same names
    # to keep track of where I am in the pseudo
    
    def initialise_positions(self):
        """
        Determines the initial positions of the boids
        """
        
    def draw_boids(self):
        """
        Renders the boids
        """
        pass
        
    def move_all_boids_to_new_positions(self):
        pass
    
    def on_loop(self):
        self.move_all_boids_to_new_positions()
     
    def on_render(self):
        self.draw_boids()
        
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        
        while(self._running):
            #Main game loop is here
            pygame.event.pump()
            self.on_loop()
            self.on_render()
            time.sleep(50.0 / 1000.0);
            
            
        self.on_cleanup()
            
if __name__ == "__main__" :
    theApp = BoidsApp()
    theApp.on_execute()