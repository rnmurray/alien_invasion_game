# alien.py
# Robyn Murray      3.29.19
# Version 1

import pygame
from pygame.sprite import Sprite

# creates an alien class for alien creation and handling
class Alien(Sprite):
    # function to create an alien
    def __init__(self, ai_settings, screen):
        #inherit from sprite
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load the alien ship image and get its rect
        self.graphic = pygame.image.load('images/alien1.png')
        self.image = pygame.transform.scale(self.graphic, (55, 55))
        self.rect = self.image.get_rect()
        
        # start alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store alien's position
        self.x = float(self.rect.x)
     
    # draw alien to screen at current position    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    # check if alien has hit an edge
    def check_edge(self):
        # get screens rect 
        screen_rect = self.screen.get_rect()
        # check if hit right edge
        if self.rect.right >= screen_rect.right:
            return True
        # check if hit left edge
        elif self.rect.left <= 0:
            return True
        
    # move alien to right or left
    def update(self):
        # increment x (by velocity factor times the direction incrementer)
        self.x += (self.ai_settings.alien_velocity_factor * self.ai_settings.fleet_dir)
        # set new position
        self.rect.x = self.x