# oil spill
# Hugh Smith
'''
the main file for the game
'''
# imports
import genarate_map


# varibles 

# classes
class alive:
    '''
    the class of the player and enimys
    '''
    def __init__(self, position, syimble, health_max, health):
        self.position = position
        self.syimble = syimble
        self.health_max = health_max
        self.health = health

    # move the player
    def move(self,direction):
        '''
        @param : turple
        @returns : none
        @throws : 
        '''
        pass

class enimy(alive):
    '''
    enimys
    '''
    pass

class player(alive):
    '''
    the player class
    '''
    pass

# functions

# main routine