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
from a_star import a_star, distance_between_points

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

# maths
import math

# varibles 
# the map for the game
game_map = []
# the enemys in the level
enemys = []
# positions os obsticals
obsticals = []

# the current level
level = 1

# the max distance when the enemys will start pathfinding
max_distance = 30

# path for the toutorial relitive to current file
totorial_text_path = "toutorial.txt"
totorial_text = ""

# path for the death relitive to current file
death_text_path = "death.txt"
death_text = ""

# if the player is in a fight
in_battle = False


# list of chartures that the enemys use
enemy_chars = []

# get the data for player and enemys
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
X_SIZE = 24
Y_SIZE = 80

# a storage value for the players last positon
store = ""

# index of the current enemy being fought
index_enemy = None

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
    the class of the player and enemys
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
    sub class for all of the enemys
    '''
    def __init__(self, position, symbol, health,health_max, enemy_type):
        super().__init__(position, symbol, health, health_max)
        self.enemy_type = enemy_type

    # return the path for the enemy
    def get_path(self, end):
        '''
        @param : (int, int) 
        @returns : list
        @throws : no possible path
        '''    
        # get the fastest path from the start to the end while avoiding the obsicals    
        return a_star(Y_SIZE,X_SIZE,obsticals,self.position,end)

class Player(Alive):
    '''
    the player sub class
    '''
    def __init__(self, position, symbol, health_max, health, stamina , max_stamina ):
        super().__init__(position, symbol, health_max, health)
        self.stamina  = stamina 
        self.max_stamina  = max_stamina 


# functions

# get the number of enemys for a given level
def get_dif(level):
    '''
    @param : int
    @returns : int
    @throws : valueError

    the games difficalty it will incress as the game progresses based off the equation y = 2.5 * sqrt(x-1)+1
    where x is the currnent level and y is the number of levels
    '''
    # get the difficalty based off a square root function
    difficalty = 2.5*math.sqrt(level-1)+1

    return int(difficalty)


# the monster attacking the player
def monster_attack():
    # the monster attacking the player
    global data_main, button_attacks, exit_button, index_enemy, continue_fight
    continue_fight.pack_forget()

    # get monster data
    monster_data = data_main["enemys"][enemys[index_enemy].enemy_type]["inventory"]

    # get the move
    move = random.choice(list(monster_data))

    # get the ammount of damage that the player will receve
    damage = random.randint(monster_data[move]["damage_min"],monster_data[move]["damage_max"])

    # damage the player
    player.health -= damage
    
    # remove the fight buttons
    for button in button_attacks:
        button.pack_forget()

    # update the gui to display corect infomation   
    exit_button.pack()
    game_text_box.config(state = "normal")    
    game_text_box.delete("1.0",END)

    text = """%s used %s the attack did %d points of damage.
you are now on %d health.    
    """%(enemys[index_enemy].enemy_type, move, damage, player.health) 
   

    game_text_box.insert(END,text) 
    game_text_box.config(state="disabled")


# the player attacking
def attack_player(button):
    global in_battle, button_attacks,game_map,store, index_enemy, continue_fight

    # check if the player is dead
    if not player.is_alive():
        for button in button_attacks:
            button.pack_forget()
            return
    
    # update the gui
    game_text_box.config(state = "normal")    
    game_text_box.delete("1.0",END)
    
    # get the move that the player is useing
    move = button.config('text')[-1]
    
    # get the damage that the move does too the enemy
    damage = random.randint(int(data_main["player"]["inventory"][move]["damage_min"]),int(data_main["player"]["inventory"][move]["damage_max"]))
    print("enemy hp",enemys[index_enemy].health)

    # decress the enemys haelth by the ammount of damage that the player does
    enemys[index_enemy].health -= damage
    print("enemy hp",enemys[index_enemy].health)

    # decress the players stamana by the amount that the move used
    player.stamina -= data_main["player"]["inventory"][move]["stamana_drain"]

    # making sure that the players stamina does not exceed the max stanana
    if player.stamina > player.max_stamina:
        player.stamina = player.max_stamina
    elif player.stamina <= 0:
        # remove the attack buttons
        for button in button_attacks:
            button.pack_forget()
        # call the players death if stamana is less than 0
        player_death()

    # update the gui
    text = '''You used %s.\n
%s\n
%s does %d damage to the %s and used %d stamina.\n
the %s is now on %d health.
you are now on %d stamana.'''%(move,data_main["player"]["inventory"][move]["description"],move,damage,enemys[index_enemy].enemy_type,data_main["player"]["inventory"][move]["stamana_drain"],enemys[index_enemy].enemy_type,enemys[index_enemy].health,player.stamina)
    for button in button_attacks:
            button.pack_forget()
    
    # if the player wins the fight
    if enemys[index_enemy].is_alive() == False:
        print("dead")
        in_battle = False
        print("the enemy is: ", game_map[enemys[index_enemy].position[1]][enemys[index_enemy].position[0]])
        game_map[enemys[index_enemy].position[1]][enemys[index_enemy].position[0]] = "#"
        store = "#"
        print("the enemy is: ", game_map[enemys[index_enemy].position[1]][enemys[index_enemy].position[0]])
        
        # give the the player a random move from the enemy
        move_to_give = random.choice(list(data_main["enemys"][enemys[index_enemy].enemy_type]["inventory"]))


        # remove the battle buttons
        for button in button_attacks:
            button.pack_forget()
        
        # give the player a move if thay dont have it allready
        if move_to_give in list(data_main["player"]["inventory"]):
            print("got move")
            text = "you defeted the %s\nthis is a very good thing because the amount of oil has been depleted good job\n\nClick any button to continue."%enemys[index_enemy].enemy_type
        else:
            data_main["player"]["inventory"][move_to_give] = data_main["items"]["wepons"][move_to_give]
            text = "you defeted the %s\nthis is a very good thing because the amount of oil has been depleted good job.\n\nyou have also gained a new move %s\n%s\n\nClick any button to continue."%(enemys[index_enemy].enemy_type, move_to_give, data_main["items"]["wepons"][move_to_give]["description"])
        # remove the enemy from the list    
        enemys.pop(index_enemy)
        
        # check to see if all enemys are dead
        if len(enemys) == 0:
            print("end level")
            text += "\n\n\n\nYou have now completed the level.\nYou have cleaned up all of the oil in this level\nyou will now be moved onto a harder level."
        
        # disable the text box
        game_text_box.insert(END,text) 
        game_text_box.config(state="disabled") 
        
        
        # set player health back up to max
        if player.is_alive():
            player.health =player.health_max
        
        return
    
    # let the player decide when to contine the fight
    continue_fight.pack()

    # disable the text box
    game_text_box.insert(END,text) 
    game_text_box.config(state="disabled")   

    # show the player thir stats
    display_stats()

# fight a monster
def battle():
    global in_battle, button_attacks, exit_button, index_enemy      
    
    # remove the exit button if it is on screen at the current point
    if exit_button.winfo_viewable():
        exit_button.pack_forget()
    game_text_box.config(state = "normal")    
    game_text_box.delete("1.0",END)
    
    # check if the player is dead
    if not player.is_alive():
        player_death()

    # find the index of the enemy that is in the battle
    index_enemy = "none"
    for i in range(len(enemys)):
        if enemys[i].position == player.position:
            index_enemy = i
            break

    # update the gui
    text = '''You are in a fight.\nYou need to kill the %s to clean up the oil!\nThe %s has got %d health.\n
click on the buttons below to use a move.
    '''%(enemys[index_enemy].enemy_type,enemys[index_enemy].enemy_type,enemys[index_enemy].health)
    
    game_text_box.insert(END,text)
    # disable editing of the text box
    game_text_box.config(state = "disabled")
    game_text_box.pack()

    # display the players updated stats
    display_stats() 
    
    # display the players possible moves
    
    button_attacks = []
    for move in data_main["player"]["inventory"]:
        print(data_main["player"]["inventory"][move])
        button_attacks.append(Button(root, text = move))
        button_attacks[-1]["command"] = lambda move_in = button_attacks[-1]: attack_player(move_in)
    for button in button_attacks:
        button.pack()
  
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
    display_stats()
    # enable the text box to edit
    game_text_box.config(state = "normal")
    # clear the text box
    game_text_box.delete("1.0",END)
    # add some text
    game_text_box.insert(END,death_text)
    # disable editing of the text box
    game_text_box.config(state = "disabled")
    game_text_box.pack()
    
# display the stats for the level and player
def display_stats():
    # display stats
    stats_box.config(state = "normal")

    # clear the text box
    stats_box.delete("1.0",END)    
    
    stats_box.insert(INSERT,"health : %d\nstamina : %d\nlevel : %d\nenemys : %d"%(player.health,player.stamina, level, len(enemys)))
    
    stats_box.config(state = "disabled")

# genarate a level
def genarate_level(difficalty):
    '''
    @param : float
    @returns : none
    @throws : valueError
    '''
    global game_map, enemys, store, enemy_types, data_main, obsticals
    # create the map and the land places
    game_map, land_pos, obsticals = genarate_map.get_map(0.01,X_SIZE,Y_SIZE)

    #set the player position
    player.position = random.choice(land_pos)

    # set a starting store value
    store = game_map[player.position[1]][player.position[0]]

    # place the player on to the map
    game_map[player.position[1]][player.position[0]] = player.symbol

    # generate the enemys and place them on to the map
    enemys = []
    for i in range(int(difficalty)):
        # choose a random enemy and add them into the map
        enemy_current_type = random.choice(enemy_types)
        enemy_current = data_main["enemys"][enemy_current_type]
        enemys.append(Enemy(random.choice(land_pos),enemy_current["symbol"],enemy_current["health"],enemy_current["health"],enemy_current_type))
        game_map[enemys[i].position[1]][enemys[i].position[0]] = enemys[i].symbol
    

# pick up keybord input
def Key_pressed(event):
    global level
    
    # check to seei fif the level has been betten 
    if len(enemys) == 0:
        print("end")
        level += 1
        genarate_level(get_dif(level))
    print(player.is_alive())

    # update the map only if the player is not dead
    if player.is_alive() and not in_battle:
        print(player.is_alive())
        update_map(event.char.lower())




# update the map
def update_map(char):
    '''
    @param : str
    @returns : none
    @throws : valueError
    '''
    global store, game_map, player, enemys, in_battle, obsticals, max_distance, button_attacks

    # check to see if the player is alive
    if not player.is_alive():
        for button in button_attacks:
            button.pack_forget()
        return

    # move the enemys by generating a path
    print(enemys)
    for enemy in enemys:
        # check the distance to the enemys  
        if distance_between_points(enemy.position, player.position) < max_distance and store != " ":
            path = enemy.get_path(player.position)
            print(path)
            # check if the there is a possible
            if path != "no possible path" and len(path) > 2:
                game_map[enemy.position[1]][enemy.position[0]] = "#"
                enemy.position = path[-2]
                game_map[enemy.position[1]][enemy.position[0]] = enemy.symbol

    # enable the text box to edit
    game_text_box.config(state = "normal")
    # clear the text box
    game_text_box.delete("1.0",END)

    # set the current players position to the stored char that was there
    game_map[player.position[1]][player.position[0]] = store
    # move the player
    player.move(user_input.movement_input(char),X_SIZE,Y_SIZE)
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
    
    display_stats()    

# main routine

# create the player
player = Player((0,0),data_main["player"]["symbol"],data_main["player"]["health_max"],data_main["player"]["health"],data_main["player"]["stamina"],data_main["player"]["stamina_max"])

# create the map and the land places
game_map, land_pos, obsticals = genarate_map.get_map(0.01,X_SIZE,Y_SIZE)

# get the enemys symbles
enemy_types = list(data_main["enemys"].keys())
for item in data_main["enemys"]:
    enemy_chars.append(data_main["enemys"][item]["symbol"])

genarate_level(get_dif(level))

# set up the gui
game_text_box.place(in_=root, anchor="c", relx=.5, rely=.5)
root.configure(bg='light blue')
root.geometry("1920x1080") 

# exit button
exit_button = Button(root, text = "continue", command = battle)

continue_fight = Button(root, text = "continue", command = monster_attack)

stats_box.place(in_=root, anchor="c", relx=1, rely=0.1)

stats_box.config(width = "39", height = "5")

stats_box.insert(INSERT,"health : %d\nstamina : %d"%(player.health,player.stamina))

stats_box.config(state = "disabled")

# bind the action of pressing a key to the keypressed function
root.bind("<KeyRelease>",Key_pressed)  

# show the map
update_map(" ")

# show the totorial
totorial(totorial_text)

# start the main routine
mainloop()