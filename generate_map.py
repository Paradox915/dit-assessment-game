# testing perlin noise V2
# Hugh Smith
'''
testing the use of perlin noise in train gen
'''

# imports 

import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise



# varibles
def get_map(_max = 0, map_x = 20, map_y = 20):

    noise1 = PerlinNoise(octaves=3)
    noise2 = PerlinNoise(octaves=6)
    noise3 = PerlinNoise(octaves=12)
    noise4 = PerlinNoise(octaves=24)

    _map = []

    # main routine
    for i in range(map_x):
        row = []
        for j in range(map_y):
            noise_val =         noise1([i/map_x, j/map_y])
            noise_val += 0.5  * noise2([i/map_x, j/map_y])
            noise_val += 0.25 * noise3([i/map_x, j/map_y])
            noise_val += 0.125* noise4([i/map_x, j/map_y])
            row.append(noise_val)
        _map.append(row)


    for x in range(map_x):
        for y in range(map_y):
            #print(_map[x][y])
            if _map[x][y] > _max:
                _map[x][y] = "#"
            else:
                _map[x][y] = " "
    return _map

if __name__ == "__main__":
    for row in get_map():
        print(*row)
