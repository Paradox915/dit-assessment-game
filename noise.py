# noise
# Hugh

'''
file for handling noise generation
'''
# imports
import random


# varibles 


# functions
# get the noise for a given map size
def get_noise1d(_min, _max, step, ajusted_strgenth):
    '''
    @param : float
    @returns : list
    @throws : 
    '''
    # set up the list that will contain the game map
    game_map = []

    # add random values into the list
    i = _min
    while i <= _max:
        game_map.append(random.random())

        i += step
        
    #print(game_map)

    # ajuste
    for value in range(len(game_map)):
        for i in range(ajusted_strgenth):
            if value != 0:
                game_map[value] = (game_map[value] + game_map[value-1])/2

    return game_map

# main routine
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    numbers = get_noise1d(0,1000000,1,5)

    plt.plot(numbers)
    plt.show()