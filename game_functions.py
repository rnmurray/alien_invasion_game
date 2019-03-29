# game_functions.py
# Robyn Murray      3.26.19
# Version 1

import sys
import pygame
from bullet import Bullet

#######################################################################
# create a function that checks for Keydown events
def check_keydown(event, ai_settings, screen, ship, bullets):
    # user pressed right key
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    # user pressed left key
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    # user pressed space bar
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    # user pressed Q key
    elif event.key == pygame.K_q:
        sys.exit()

# create a function that checks for Keyup events        
def check_keyup(event, ship):
    # user released right key
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    # user released left key
    elif event.key == pygame.K_LEFT:
        ship.move_left = False

# create a function to respond to keyboard and mouse events
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # check for keyboard down press
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullets)
        # check for keyboard release        
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


#######################################################################

#update images on the screen and send to the new screen            
def screen_update(ai_settings, screen, ship, alien, bullets):
    # fill background of the screen
    screen.fill(ai_settings.bg_color)
    #draw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # add ship to screen
    ship.blitme()
    # add alien to screen
    alien.blitme()
    # update the surface to the screen
    pygame.display.flip()

#update bullet positions and remove bullets on screen to preserve memory    
def refresh_bullets(bullets):
    #update bullet screen positions
    bullets.update()
    
    # get rid of bullets that are above the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
# function that fires allowed number of bullets
def fire_bullets(ai_settings, screen, ship, bullets):
    # check if number of bullets is less than permitted
    if len(bullets) < ai_settings.bullets_permitted:
        # create new bullet and add
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)