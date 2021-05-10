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

#randomness
import random

# time
import time

# varibles 
game_map = []
enemys = []

totorial_text_path = "toutorial.txt"
totorial_text = ""

# open and get the totorial text
with open (totorial_text_path, "r") as file:
    totorial_text=file.read()

# the x and y size of the map
x_size = 24 # 24
y_size = 80 # 80

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
        @param : none
        @returns : bool
        @throws : none
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
    # return the path for the enemy
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
    def __init__(self, position, symbol, health_max, health, stamina , max_stamina ):
        super().__init__(position, symbol, health_max, health)
        self.stamina  = stamina 
        self.max_stamina  = max_stamina 

    # get the players inventory
    def get_inventory(self):
        '''
        @param : 
        @returns :
        @throws :
        '''
        pass

# create tkinter game_text_box 
root = Tk() 
root.title('oil spill') 

# initalise the main text box for the game screen
game_text_box = Text(root, font = ('Courier', 20, 'bold'), bg = "light blue", fg = "green", state = "disabled") 


# initalise the ui for the player's stats
stats_box = Text(root, font = ('Courier', 20, 'bold'), bg = "light blue", fg = "black", state = "disabled") 


# functions

# totorial
def totorial(text = "totorial"):
    # enable the text box to edit
    game_text_box.config(state = "normal")
    # clear the text box
    game_text_box.delete("1.0",END)
    # add some text
    game_text_box.insert(END,text)
    # disable editing of the text box
    game_text_box.config(state = "disabled")
    game_text_box.pack()

# end the game after the player has died
def player_death():
    player.health = 0
    # enable the text box to edit
    game_text_box.config(state = "normal")
    # clear the text box
    game_text_box.delete("1.0",END)
    # add some text
    game_text_box.insert(END,"you are dead")
    # disable editing of the text box
    game_text_box.config(state = "disabled")
    game_text_box.pack()
    

# genarate a level
def genarate_level(difficalty):
    '''
    @param : float
    @returns : none
    @throws : valueError
    '''
    global game_map, enemys, store
    # create the map and the land places
    game_map, land_pos = genarate_map.get_map(0.01,x_size,y_size)

    #set the player position
    player.position = random.choice(land_pos)

    # set a starting store value
    store = game_map[player.position[1]][player.position[0]]

    # place the player on to the map
    game_map[player.position[1]][player.position[0]] = player.symbol

    # generate the enemys and place them on to the map
    enemys = []
    for i in range(int(difficalty)):
        enemys.append(Enemy(random.choice(land_pos),"X",10,10))
        game_map[enemys[i].position[1]][enemys[i].position[0]] = enemys[i].symbol
    

# pick up keybord input
def Key_pressed(event):
    '''
    @parm : none
    @retruns : none
    @throws : none
    '''
    # update the map only if the player is not dead
    if player.is_alive():
        update_map(event.char)
    else:
        print("sorry you are dead")




# update the map
def update_map(char):
    '''
    @param : str
    @returns : none
    @throws : valueError
    '''
    global store, game_map, player, enemys
    # enable the text box to edit
    game_text_box.config(state = "normal")
    # clear the text box
    game_text_box.delete("1.0",END)

    # set the current players position to the stored char that was there
    game_map[player.position[1]][player.position[0]] = store
    # move the player
    player.move(user_input.movement_input(char),x_size,y_size)
    # get a new store value
    store = game_map[player.position[1]][player.position[0]]
    # place the player on the map
    game_map[player.position[1]][player.position[0]] = player.symbol



    # game logic
    # check if the player is over water
    if store == " ":
        player.stamina  -= 1
        if player.stamina  <= 0:
            print("you are dead")
            player_death()
    elif store == "X":
        print("enemy")
    else:
        if player.stamina  < player.max_stamina :
            player.stamina  += 1
    
    print("player stamina : ",player.stamina )
    # draw the map to the screen
    text = ""
    for row in game_map:
        for item in row:
            text += str(item)
        text += "\n"
    game_text_box.insert(END,text)
    # make the player a diffrent colour
    game_text_box.tag_add("player", "%d.%d"%(player.position[1]+1,player.position[0]))
    game_text_box.tag_config("player", foreground="black")

    # make the enimys a diffrent colour
    for enemy in enemys:
        game_text_box.tag_add("enemy", "%d.%d"%(enemy.position[1]+1,enemy.position[0]))
        game_text_box.tag_config("enemy", foreground="dark red")
    # disable editing of the text box
    game_text_box.config(state = "disabled")
    game_text_box.pack()



# main routine

# create the player
player = Player((0,0),"&",100,100,10,10)

# create the map and the land places
game_map, land_pos = genarate_map.get_map(0.01,x_size,y_size)

genarate_level(10)

# set up the gui
game_text_box.place(in_=root, anchor="c", relx=.5, rely=.5)
root.configure(bg='light blue')
root.geometry("1920x1080") 

stats_box.place(in_= root, anchor="c", relx=1, rely=0)

# bind the action of pressing a key to the keypressed function
root.bind("<KeyRelease>",Key_pressed)  

# show the map
update_map(" ")

totorial(totorial_text)

# start the main routine
mainloop()