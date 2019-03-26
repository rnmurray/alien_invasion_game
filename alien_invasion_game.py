# alien_invasion_game.py
# Robyn Murray      3.25.19
# Version 1


#######################################################################
# import modules
import sys

import pygame

from settings import Settings
from ship import Ship

# create a function to run the game
def run_game():
    # init game, settings, and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Create a ship
    ship = Ship(screen)
    
    # start main While loop for the game
    while True:
        
        # watch for keyboard/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # redraw the screen during each pass through loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # make most recent screen visible for smooth movement
        pygame.display.flip()
        
# call the run game function
run_game()