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
class Alive:
    '''
    the class of the player and enimys
    '''
    def __init__(self, position, symbol, health_max, health):
        self.position = position
        self.symbol = symbol
        self.health_max = health_max
        self.health = health
    
    # check if the object is alive
    def is_alive(self):
        '''
        @param : 
        @returns : bool
        @throws : 
        '''
        if self.health <= 0:
            return False
        else:
            return True
    
    # move the object
    def move(self,direction):
        '''
        @param : (int, int)
        @returns : none
        @throws : 
        '''
        pass

class Enemy(alive):
    '''
    enimys
    '''
    def get_path():
        '''
        @param : (int, int), (int, int) 
        @returns : list
        @throws : no possible path
        '''        
        pass

class Player(alive):
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