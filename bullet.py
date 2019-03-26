# bullet.py
# Robyn Murray      3.26.19
# Version 1

import pygame
from pygame.sprite import Sprite

#######################################################################

class Bullet(Sprite):
    
    # Create bullet object at ships current position
    def __init__(self, ai_settings, screen, ship):
        # inherit from Sprite init method
        super(Bullet, self).__init__()
        self.screen = screen
        
        # create bullet rect at origin then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # convert position to decimal value
        self.y = float(self.rect.y)
        
        # give the bullet a color and a speed
        self.color = ai_settings.bullet_color
        self.speed_multiplier = ai_settings.bullet_speed_multiplier
        
    # move the bullet up 
    def update(self):
        # get new decimal pos of bullet
        self.y -= self.speed_multiplier
        # update bullet rect pos
        self.rect.y = self.y
        
    # draw the bullet to the screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        