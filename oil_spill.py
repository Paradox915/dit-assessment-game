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
game_map = []

x_size = 20
y_size = 20

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
    
    # return the stats
    def get_stats(self):
        '''
        @param : 
        @returns :
        @throws :
        '''
        pass

    # move the object
    def move(self,direction, x_max, y_max):
        '''
        @param : (int, int)
        @returns : none
        @throws : TypeError
        '''
        # make sure that the player is inside of the boundary
        if self.position[0]+direction[0] < y_max and self.position[1]+direction[1] < x_max and self.position[0]+direction[0] >= 0 and self.position[1]+direction[1] >= 0:
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
    # get the players inventory
    def get_inventory(self):
        '''
        @param : 
        @returns :
        @throws :
        '''
        pass

# functions

# main routine
# create the player
player = Player((0,0),"&",100,100)

# create the map
game_map = genarate_map.get_map(0.01,x_size,y_size)

store = game_map[player.position[1]][player.position[0]]

game_map[player.position[1]][player.position[0]] = player.symbol
# playing game
playing = True
while playing:
    # play game
    # get user input
    # print the map
    for row in game_map:
        print(*row)
    game_map[player.position[1]][player.position[0]] = store
    player.move(user_input.movement_input(),x_size,y_size)
    store = game_map[player.position[1]][player.position[0]]
    game_map[player.position[1]][player.position[0]] = player.symbol
    