# alien_invasion_game.py
# Robyn Murray      3.25.19
# Version 1

# import modules
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
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
    
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    
    #Create a ship
    ship = Ship(ai_settings, screen)
    # Create a group to store bullets from sprite
    bullets = Group()
    # create a group of aliens
    aliens = Group()
    
    # create fleet of aliens
    gf.make_fleet(ai_settings, screen, ship, aliens)
    
    # start main loop for the game
    while True:
        # watch for keyboard/mouse events
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        #see if game is still active
        if stats.game_active:
            # update ship object
            ship.update()
            # remove bullets above top of screen and update positions
            gf.refresh_bullets(ai_settings, screen, ship, aliens, bullets)
            # update alien pos
            gf.refresh_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # update screen and send to new screen
        gf.screen_update(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        
# call the run game function
run_game()