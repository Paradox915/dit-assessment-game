# oil spill
# Hugh Smith
'''
the main file for the game

the game shall be about an oil spill and you have to go around
and clean up as much oil in the form of killing monsters and other means
'''
# imports
# the map genaration
import genarate_map
# the pathfinding for the enimys
import a_star

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

# playing game
playing = True
while playing:
    # play game
    pass