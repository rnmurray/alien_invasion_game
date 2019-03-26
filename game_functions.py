# game_functions.py
# Robyn Murray      3.26.19
# Version 1

import sys

import pygame

#######################################################################

# create a function to respond to keyboard and mouse events
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#update images on the screen and send to the new screen            
def screen_update(ai_settings, screen, ship):
    # fill background of the screen
    screen.fill(ai_settings.bg_color)
    # add ship to screen
    ship.blitme()
    # update the surface to the screen
    pygame.display.flip()