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
        self.bg_color = (230, 230, 230) #light gray
        
        # ship settings
        self.ship_velocity_factor = 1.5
        self.ship_limit = 3
        
        # bullet settings
        self.bullet_velocity_factor = 3
        self.bullet_width = 3
        #for testing increase bullet width
        #self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60  # dark gray
        self.bullets_permitted = 4
        
        # alien ship settings
        self.alien_velocity_factor = 1
        self.fleet_down_velocity = 10
        #self.fleet_down_velocity = 50
        # fleet direction of 1 reps right; -1 reps left, start right
        self.fleet_dir = 1