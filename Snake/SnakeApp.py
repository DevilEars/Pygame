# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:56:40 2020

@author: devilears
"""

# p key is just for debug
from pygame.locals import QUIT, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE, K_d
from random import randint

import pygame
import time

# Snake game classes
from Apple import Apple
from Player import Player
from Board import Board

 
class SnakeApp:
 
    '''
    Main class that keeps track of snakes, apples and the board.
    All the Pygame magic happens here.
    '''
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
 
    def __init__(self):
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self._running = True
        self.board = Board(self.windowWidth, self.windowHeight)
        self.player = Player(3) 
        self.apple = Apple(5,5)
        
    def print_debug(self):
        '''
        Method to print debug
        I put this in its own method because this could change all the time
        and I don't want to clutter the main execution code
        '''
        print("$$$$$$\nHola! ¿Cómo estás?")
        print(self.player.x[0])
        print(self.player.y[0])
        print("$$$$$$\n")
                
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption('No Step on Snek')
        
        # surfaces
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        self._image_surf = pygame.image.load("block.png").convert()
        self._apple_surf = pygame.image.load("apple.png").convert()
        
        # start running the game!
        self._running = True
 
    def on_event(self, event):
        # Esc key to exit
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
        
        # does snake run into walls?
        if(self.board.isPointOutsideBoard(self.player.x[0], self.player.y[0])):
            print("Your snake ran into a wall or probably fell into a pit of lava! Wall collision:")
            print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
            self._running = False
            
            
 
        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.board.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],self.player.step):
                self.apple.x = randint(2,9) * self.player.step
                self.apple.y = randint(2,9) * self.player.step
                self.player.length = self.player.length + 1
 
 
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.board.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i], self.player.step - 5):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                self._running = False
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            # move keys
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            # game flow control keys
            if (keys[K_ESCAPE]):
                self._running = False
                
            # d is for debug to see wtf is going on                    
            if (keys[K_d]):
                self.print_debug()
                
                
            self.on_loop()
            self.on_render()
            time.sleep(50.0 / 1000.0);
            
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = SnakeApp()
    theApp.on_execute()