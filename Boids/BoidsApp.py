# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:21:40 2020

@author: devilears
"""

import pygame
from pygame.locals import QUIT
import random
from Boid import Boid

class BoidsApp:
    """
    Classic Boids
    """
    boids = []
    border = 15# can still tweak this or debug bounding box
    maxDistance = 2000
    minDistance = 50
    maxVelocity = 10
    numBoids = 23
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)        
    
    
    def __init__(self):
        self.caption = 'Boids'
        
        
    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        
        # surfaces
        self.ball = pygame.image.load("fireball.png")
        #self.ball = pygame.image.load("fireball.png").convert()
        self.ballrect = self.ball.get_rect()
        
        # start running the game!
        self._running = True

    
    def on_event(self, event):
       # Esc key to exit
       # This doesn't work so well
       # Threads might be locking
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
        #print("initialise_positions")
        for i in range(self.numBoids):
            self.boids.append(Boid(random.randint(0, self.width), random.randint(self.height, self.height+5)))
            #self.boids.append(Boid(random.randint(0, self.width), random.randint(0, self.height)))
        
    def draw_boids(self):
        """
        Renders the boids
        """
        #print("draw boids")
        self.screen.fill((0, 0, 0))
        for boid in self.boids:
            boidRect = pygame.Rect(self.ballrect)
            boidRect.x = boid.x
            boidRect.y = boid.y
            self.screen.blit(self.ball, boidRect)
        pygame.display.flip()
        
        
    def move_all_boids_to_new_positions(self):
        """
        All the magic happens here. This determines neighbouring boids,
        and performs all the boid emergent functions while we're in the loop
        """
        #print("move boids to new positions")
        for boid in self.boids:
            closeBoids = []
            for otherBoid in self.boids:
                if otherBoid == boid: continue
                distance = boid.distance(otherBoid)
                if distance < self.maxDistance:
                    closeBoids.append(otherBoid)
    
            
            boid.moveCloser(closeBoids)
            boid.moveWith(closeBoids)  
            boid.moveAway(closeBoids, self.minDistance)
            
            if boid.x < self.border and boid.velocity_x < 0:
                boid.velocity_x = -boid.velocity_x * random.random()
            if boid.x > self.width - self.border and boid.velocity_x > 0:
                boid.velocity_x = -boid.velocity_x * random.random()
            if boid.y < self.border and boid.velocity_y < 0:
                boid.velocity_y = -boid.velocity_y * random.random()
            if boid.y > self.height - self.border and boid.velocity_y > 0:
                boid.velocity_y = -boid.velocity_y * random.random()
            
            boid.move(self.maxVelocity)

    
    def on_loop(self):
        self.move_all_boids_to_new_positions()
     
    def on_render(self):
        self.draw_boids()
        
        
    def on_cleanup(self):
        #print("kthxbi")
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        self.initialise_positions()
        while(self._running):
            #Main game loop is here
            pygame.event.pump()
            
            self.on_render()
            self.on_loop()
            
            pygame.time.delay(50)
            
            
        self.on_cleanup()
            
if __name__ == "__main__" :
    theApp = BoidsApp()
    theApp.on_execute()