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

# json
import json
# varibles 
game_map = []
enemys = []

totorial_text_path = "toutorial.txt"
totorial_text = ""

death_text_path = "death.txt"
death_text = ""

# if the player is in a fight
in_battle = False


# list of chartures that the enemys use
enemy_chars = []

data_main_path = "data_main.json"
# open and get the totorial text
with open (totorial_text_path, "r") as file:
    totorial_text=file.read()
    
    
# open and get the totorial text
with open (death_text_path, "r") as file:
    death_text=file.read()


# get the data in the json file
with open(data_main_path) as file:
    data_main = json.load(file)

# the x and y size of the map
x_size = 24 # 24
y_size = 80 # 80

store = ""

# the buttons
button_attacks = []

# create tkinter game_text_box 
root = Tk() 
root.title('oil spill') 

# initalise the main text box for the game screen
game_text_box = Text(root, font = ('Courier', 20, 'bold'), bg = "light blue", fg = "green", state = "disabled") 


# initalise the ui for the player's stats
stats_box = Text(root, font = ('Courier', 20, 'bold'), bg = "light blue", fg = "black", state = "normal") 

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
    def __init__(self, position, symbol, health, stamina,health_max, enemy_type):
        super().__init__(position, symbol, health, health_max)
        self.stamina  = stamina 
        self.enemy_type = enemy_type
        #self.health = health
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


# functions
# the player attacking
def attack_player(move,index_enemy):
    game_text_box.config(state = "normal")    
    game_text_box.delete("1.0",END)
    #print("the move: ", move)
    print("the enemy: ", enemys[index_enemy])
    damage = random.randint(data_main["player"]["inventory"][move]["damage_max"],data_main["player"]["inventory"][move]["damage_min"])
    text = '''You used %s
%s does %d damage to the %s and used %d stamina
the %s is now on %d health'''%(move,move,damage,enemys[index_enemy].enemy_type,data_main["player"]["inventory"][move]["stamana_drain"],enemys[index_enemy].enemy_type,enemys[index_enemy].health)
    print("move name is",button_attacks[0].config('text')[-1])    
    game_text_box.insert(END,text)    
# fight a monster
def battle():
    global in_battle, button_attacks      
    # get which enemy that the player is figthing
    game_text_box.config(state = "normal")    
    game_text_box.delete("1.0",END)
    
    # find the index of the enemy that is in the battle
    index_enemy = "none"
    for i in range(len(enemys)):
        if enemys[i].position == player.position:
            index_enemy = i
            break

    text = '''You are in a fight.\nYou need to kill the %s to clean up the oil!\nThe %s has got %d health
    '''%(enemys[index_enemy].enemy_type,enemys[index_enemy].enemy_type,enemys[index_enemy].health)
    
    game_text_box.insert(END,text)
    # disable editing of the text box
    game_text_box.config(state = "disabled")
    game_text_box.pack()    
    
    # display the players possible moves
    
    button_attacks = []
    for move in data_main["player"]["inventory"]:
        print(data_main["player"]["inventory"][move])
        button_attacks.append(Button(root, text = move, command = lambda: attack_player(move,index_enemy)))
    for button in button_attacks:
        button.pack()
        print("move name is",button.config('text')[-1])
  
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
    game_text_box.insert(END,death_text)
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
    global game_map, enemys, store, enemy_types, data_main
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
        enemy_current_type = random.choice(enemy_types)
        enemy_current = data_main["enemys"][enemy_current_type]
        #print(enemy_current)
        enemys.append(Enemy(random.choice(land_pos),enemy_current["symbol"],enemy_current["health"],enemy_current["stamina"],enemy_current["health"],enemy_current_type))
        game_map[enemys[i].position[1]][enemys[i].position[0]] = enemys[i].symbol
    

# pick up keybord input
def Key_pressed(event):
    '''
    @parm : none
    @retruns : none
    @throws : none
    '''
    # update the map only if the player is not dead
    if player.is_alive() and not in_battle:
        update_map(event.char)




# update the map
def update_map(char):
    '''
    @param : str
    @returns : none
    @throws : valueError
    '''
    global store, game_map, player, enemys, in_battle
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
    elif store in enemy_chars:
        print("enemy")
        in_battle = True
        battle()
    else:
        if player.stamina  < player.max_stamina :
            player.stamina  += 1
    
    # print("player stamina : ",player.stamina )
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
    
    # display stats
    stats_box.config(state = "normal")

    # clear the text box
    stats_box.delete("1.0",END)    
    
    stats_box.insert(INSERT,"health : %d\nstamina : %d"%(player.health,player.stamina))
    
    stats_box.config(state = "disabled")    

# main routine

# create the player
player = Player((0,0),"&",100,100,20,20)

# create the map and the land places
game_map, land_pos = genarate_map.get_map(0.01,x_size,y_size)

# get the enemys symbles
enemy_types = list(data_main["enemys"].keys())
for item in data_main["enemys"]:
    enemy_chars.append(data_main["enemys"][item]["symbol"])

genarate_level(10)

# set up the gui
game_text_box.place(in_=root, anchor="c", relx=.5, rely=.5)
root.configure(bg='light blue')
root.geometry("1920x1080") 


stats_box.place(in_=root, anchor="c", relx=1, rely=0.1)

stats_box.config(width = "39", height = "5")

stats_box.insert(INSERT,"health : %d\nstamina : %d"%(player.health,player.stamina))

stats_box.config(state = "disabled")

# bind the action of pressing a key to the keypressed function
root.bind("<KeyRelease>",Key_pressed)  

# show the map
update_map(" ")

totorial(totorial_text)

# start the main routine
mainloop()