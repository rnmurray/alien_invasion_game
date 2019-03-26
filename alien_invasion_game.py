# alien_invasion_game.py
# Robyn Murray      3.25.19
# Version 1

# import modules
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf     # alias for game functions

#######################################################################
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
        gf.check_events()
        # update screen and send to new screen
        gf.screen_update(ai_settings, screen, ship)
        
# call the run game function
run_game()