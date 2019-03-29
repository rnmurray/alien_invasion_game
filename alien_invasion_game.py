# alien_invasion_game.py
# Robyn Murray      3.25.19
# Version 1

# import modules
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
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
    ship = Ship(ai_settings, screen)
    # Create a group to store bullets from sprite
    bullets = Group()
    # create an alien
    alien = Alien(ai_settings, screen)
    
    # start main loop for the game
    while True:
        # watch for keyboard/mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        # update ship object
        ship.update()
        # remove bullets above top of screen and update positions
        gf.refresh_bullets(bullets)
        # update screen and send to new screen
        gf.screen_update(ai_settings, screen, ship, alien, bullets)
        
# call the run game function
run_game()