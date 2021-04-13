# testing perlin noise V2
# Hugh Smith
'''
testing the use of perlin noise in train genaration
'''

# imports 
from perlin_noise import PerlinNoise



# varibles
def get_map(_max = 0.001, map_x = 100, map_y = 100):

    noise1 = PerlinNoise(octaves=3)
    noise2 = PerlinNoise(octaves=6)
    noise3 = PerlinNoise(octaves=12)

    _map = []

    # main routine
    for x in range(map_x):
        row = []
        for y in range(map_y):
            noise_val = noise1([x/map_x, y/map_y])
            noise_val += 0.5  * noise2([x/map_x, y/map_y])
            noise_val += 0.25 * noise3([x/map_x, y/map_y])
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
