# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:21:40 2020

@author: devilears
"""

import pygame

class BoidsApp:
    """
    Classic Boids
    """
    caption = 'Boids'#Title of window
    
    def __init__(self):
        self.caption = ''
        
    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        
        # surfaces

        
        # start running the game!
        self._running = True

    
    def on_event(self, event):
        # Esc key to exit
        if event.type == QUIT:
            self._running = False    

    def on_loop(self):
         
         pass
     
    def on_render(self):
        
        
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        
        while(self._running):
            #Main game loop is here
            self.on_loop()
            self.on_render()
            time.sleep(50.0 / 1000.0);
            
            
        self.on_cleanup()
            
if __name__ == "__main__" :
    theApp = BoidsApp()
    theApp.on_execute()