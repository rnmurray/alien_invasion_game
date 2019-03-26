# ship.py
# Robyn Murray      3.25.19
# Version 1

import pygame

# creates a ship class for ship creation and starting position
class Ship():
    
    # make init function including screen
    def __init__(self, screen):
        self.screen = screen
        
        # load ship image and get its rect
        self.graphic = pygame.image.load('images/ship.bmp')
        self.rect = self.graphic.get_rect()
        self.screen_rect = screen.get_rect()
        
        # start each ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    # make a function to draw ship at its current location
    def blitme(self):
        self.screen.blit(self.graphic, self.rect)