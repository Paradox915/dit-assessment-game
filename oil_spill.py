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

# the gui
from tkinter import * 

# varibles 
game_map = []

x_size = 20
y_size = 20

store = ""
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
    def __init__(self, position, symbol, health_max, health, stamana, max_stamana):
        super().__init__(position, symbol, health_max, health)
        self.stamana = stamana
        self.health_max = max_stamana

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

# create tkinter window 
root = Tk() 
root.title('dit game') 

window = Label(root, font = ('Cascadia Mono', 30, 'bold'), 
            background = 'light blue', 
            foreground = 'green',) 


# functions
# pick up keybord imput
def Key_pressed(event):
    '''
    @parm : none
    @retruns : none
    @throws : none
    '''
    print(event.char)
    player.move(user_input.movement_input(event.char),x_size,y_size)
    update_map()




# update the map
def update_map():
    global store, game_map,player
    game_map[player.position[1]][player.position[0]] = store
    store = game_map[player.position[1]][player.position[0]]
    game_map[player.position[1]][player.position[0]] = player.symbol
    text = ""
    for row in game_map:
        for item in row:
            text += str(item)
        text += "\n"
    window.config(text = text)

# main routine

# create the player

player = Player((0,0),"&",100,100,100,100)

# create the map
game_map = genarate_map.get_map(0.01,x_size,y_size)

store = game_map[player.position[1]][player.position[0]]

game_map[player.position[1]][player.position[0]] = player.symbol

window.place(in_=root, anchor="c", relx=.5, rely=.5)
root.configure(bg='light blue')
root.geometry("1920x1080") 

# bind the action of pressing a key to the keypressed function
root.bind("<KeyRelease>",Key_pressed)  

mainloop() 
    