# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:22:07 2020

@author: devilears
"""
import pygame
from pygame.locals import QUIT, K_ESCAPE

class App:
    """
    Template for App using Pygame
    This is meant to cuntpaste and embellish, not for fancy OOP
    """
    
    def __init__(self):
        self.caption = ''
        
    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        
        # surfaces

        
        # start running the game!
        self._running = True

    
    def on_event(self, event):
        # Event when window is closed
        # This is iffy
        if event.type == QUIT:
            self._running = False    

    def on_loop(self):
         pass
     
    def on_render(self):
        pass
        
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        
        while(self._running):
             # main game loop is here
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            # when user bails with Esc key
            if (keys[K_ESCAPE]):
                self._running = False
            
            self.on_loop()
            self.on_render()
            
            # game clock delay
            pygame.time.delay(50)
            
            
        self.on_cleanup()
            
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()