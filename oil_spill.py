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

# handle user input
import user_input

# varibles 
_map_store = []
_map = []
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
        print(direction)
        self.position = (self.position[0]+direction[0],self.position[1]+direction[1])


class Enemy(Alive):
    '''
    enimys
    '''
    def get_path(self):
        '''
        @param : (int, int), (int, int) 
        @returns : list
        @throws : no possible path
        '''        
        pass

class Player(Alive):
    '''
    the player class
    '''
    pass

# functions

# main routine
# create the player
player = Player((0,0),"&",100,100)

# create the map
_map = genarate_map.get_map()

_map_store = _map.copy()

_map[player.position[1]][player.position[0]] = player.symbol
# playing game
playing = True
while playing:
    # play game
    # get user input
    print("map")
    for row in _map:
        print(*row)
    print("store")
    for row in _map_store:
        print(*row)
    #print(player.position)
    old_char =  _map_store[player.position[1]][player.position[0]]
    _map[player.position[1]][player.position[0]] = old_char
    print(player.position)
    player.move(user_input.movement_input())
    print(player.position)
    _map[player.position[1]][player.position[0]] = player.symbol
    