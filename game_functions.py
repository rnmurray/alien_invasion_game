# game_functions.py
# Robyn Murray      3.26.19
# Version 1

import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

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
def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        # check for keyboard down press
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullets)
        # check for keyboard release        
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

#check if user clicked on button
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # mouse was pushed within button rect
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    # see if game is already going and there is a button click
    if button_click and not stats.game_active:
        #hide mouse
        pygame.mouse.set_visible(False)
        #activate game and reset
        stats.reset_stats()
        stats.game_active = True
        #clear list of aliens/bullets
        aliens.empty()
        bullets.empty()
        #make new fleet center ship
        make_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

#######################################################################

# function that fires allowed number of bullets
def fire_bullets(ai_settings, screen, ship, bullets):
    # check if number of bullets is less than permitted
    if len(bullets) < ai_settings.bullets_permitted:
        # create new bullet and add
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# calc num of aliens that fit in a row        
def get_num_aliens_x(ai_settings, alien_width):
    # allow for a margin of one alien each side of screen
    space_avail_x = ai_settings.screen_width - (2 * alien_width)
    # get number of aliens in row (space of one alien between)
    num_aliens_x = int(space_avail_x / (2 * alien_width))
    return num_aliens_x

# calc num of rows avail
def get_num_rows_y(ai_settings, ship_height, alien_height):
    # subtract 2 alien heights from bottom inc ship and subtract one more from top
    space_avail_y = (ai_settings.screen_height - (2 * alien_height) - alien_height - ship_height)
    # space each row by one alien height
    num_rows_y = int(space_avail_y / (2 * alien_height))
    return num_rows_y

#make an alien and add it to row
def make_alien(ai_settings, screen, aliens, alien_num, row_num):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # set postion of x coord of alien
    alien.x = alien_width + (2 * alien_width * alien_num)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_num)
    # add alien to group
    aliens.add(alien)
        
# make a fleet of aliens        
def make_fleet(ai_settings, screen, ship, aliens):
    # make alien and get num of aliens that fit in row and num of rows fit in screen
    alien = Alien(ai_settings, screen)
    num_aliens_x = get_num_aliens_x(ai_settings, alien.rect.width)
    num_rows_y = get_num_rows_y(ai_settings, ship.rect.height, alien.rect.height)
    
    # make fleet with nested loop
    for row_num in range(num_rows_y):
        for alien_num in range(num_aliens_x):
            make_alien(ai_settings, screen, aliens, alien_num, row_num)
            
# check if fleet is hitting edge
def check_fleet_edge(ai_settings, aliens):
    #loop through all aliens
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_dir(ai_settings, aliens)
            break
    
# drop fleet down and change direction
def change_fleet_dir(ai_settings, aliens):
    # move fleet down by velocity factor
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_down_velocity
    # change the sign of the direction value
    ai_settings.fleet_dir *= -1

# see when bullets and aliens collide then delete both items    
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # check for bullets that have hit aliens
    # if bullet hit, remove bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #for testing dont kill bullet till after it hits the top
    #collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

# do things when alien hits ship
def hit_ship(ai_settings, stats, screen, ship, aliens, bullets):
    #check num of ships
    if stats.ships_rem > 1:
        # take away one ship
        stats.ships_rem -= 1
        # get rid of all aliens and bullets on screen
        aliens.empty()
        bullets.empty()
        # make a new fleet and center the ship
        make_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause game a certain amount of secs
        sleep(1)
    # game is over 
    else:
        stats.game_active = False
        # bring back mouse
        pygame.mouse.set_visible(True)
        
# check if alien touches bottom of screen
def check_bottom_touch(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    #loop to check all aliens
    for alien in aliens.sprites():
        # alien touches bottom
        if alien.rect.bottom >= screen_rect.bottom:
            # act as if ship is hit
            hit_ship(ai_settings, stats, screen, ship, aliens, bullets)
            break
#####################################################################

#update images on the screen and send to the new screen            
def screen_update(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    # fill background of the screen
    screen.fill(ai_settings.bg_color)
    #draw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # add ship to screen
    ship.blitme()
    # draw alien to screen
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    # update the surface to the screen
    pygame.display.flip()

#update bullet positions and get rid of unneeded ones    
def refresh_bullets(ai_settings, screen, ship, aliens, bullets):
    #update bullet screen positions
    bullets.update()
    # get rid of bullets that are above the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    # call check for collision function to remove hits
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
    #check to see if fleet if gone
    if len(aliens) == 0:
        # remove all bullets and make new fleet
        bullets.empty()
        make_fleet(ai_settings, screen, ship, aliens)

# update pos of all aliens in fleet          
def refresh_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    # check if any aliens hitting edge
    check_fleet_edge(ai_settings, aliens)
    # update pos
    aliens.update()
    # look if alien hit ship
    if pygame.sprite.spritecollideany(ship, aliens):
        hit_ship(ai_settings, stats, screen, ship, aliens, bullets)
        
    # look if any alien touches screen bottom
    check_bottom_touch(ai_settings, stats, screen, ship, aliens, bullets)
    
            
            
