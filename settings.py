# settings.py
# Robyn Murray      3.25.19
# Version 1

# creates a settings class for modifying game settings in Alien invastion
class Settings():
    
    #initialize function for game's settings
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # ship settings
        self.ship_speed_multiplier = 1.5