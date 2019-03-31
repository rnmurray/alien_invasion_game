#button.py
#Robyn Murray
#Version 1          3/31/2019

import pygame.font

######################################################################
#creates a button for use in a game
class Button():
    
    #initialize button
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #set dimensions and properties of button
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #make buttons rect object and center on screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #button message needs to be prepped just once
        self.write_msg(msg)
    
    #function to render message on button    
    def write_msg(self, msg):
        # turn message into a rendered image
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # center text on the button
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    #method to display button on the screen
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)