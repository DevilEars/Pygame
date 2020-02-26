"""
Created on Thu Feb 13 17:22:07 2020

@author: devilears
"""
import pygame
import numpy as np
import matplotlib.pyplot as plt
from pygame.locals import QUIT, K_ESCAPE

class GameOfLifeApp:
    """
    Conway's Game of Life. A bit of an useless machine as far as gaming goes
    """
    
    def __init__(self):
        self.caption = 'Game of Life'
        self.generations = 70
        self.cells = 6
        
    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        
        # start running the game!
        self._running = True

    def create_universe(self):
        """
        Initialises the grid
        """
        print('create_universe()')
        self.universe = np.zeros((self.cells, self.cells))
        
    def add_beacon(self):
        """
        Creates a Beacon and adds it to the universe
        """
        print('add_beacon()')
        beacon = [[1,1,0,0],
                  [1,1,0,0],
                  [0,0,1,1],
                  [0,0,1,1]]
        self.universe[1:5, 1:5] = beacon
        

    def seed_universe(self):
        """
        Places automatons in the universe
        """
        self.add_beacon()
        
        
    
        

    def fitness_test(self):
        pass

    
    def on_event(self, event):
        # Event when window is closed
        # This is iffy
        if event.type == QUIT:
            self._running = False    

    def on_loop(self):
         pass
     
    def on_render(self):
        plt.imshow(self.universe, cmap='binary')
        plt.show()
        
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        self.create_universe()
        self.seed_universe()
        
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
    theApp = GameOfLifeApp()
    theApp.on_execute()