#game_stats.py
#Robyn Murray
#Version 1      3/31/2019

#######################################################################
#This class tracks statistics for Alien Invasion game
class GameStats():
    #method to init class statistics
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #start out game in inactive state
        self.game_active = False
    
    #initialize stats that can change during game    
    def reset_stats(self):
        self.ships_rem = self.ai_settings.ship_limit