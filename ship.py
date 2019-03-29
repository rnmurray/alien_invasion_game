# ship.py
# Robyn Murray      3.25.19
# Version 1

import pygame

# creates a ship class for ship creation and handling
class Ship():
    
    # make init function including screen
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load ship image and scale to desired size (w, h)
        self.graphic = pygame.image.load('images/ship2.png')
        self.image = pygame.transform.scale(self.graphic, (75, 125))
        
        # get ship as rect and screen as rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # start each ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # convert ship center to decimal value
        self.center = float(self.rect.centerx)
        
        # create movement flags to check for left/right keypress
        self.move_right = False
        self.move_left = False
        
    # update ships position if movement flag is true
    def update(self):
        # update ships center value
        # check if ship x right edge is less than right edge of screen
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_multiplier
        # check if ship x left edge is more than left edge
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_multiplier
        # now update rect object from center   
        self.rect.centerx = self.center
        
    # make a function to draw ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)