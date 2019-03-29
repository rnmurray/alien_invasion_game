# alien.py
# Robyn Murray      3.29.19
# Version 1

import pygame
from pygame.sprite import Sprite

# creates an alien class for alien creation and handling
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
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