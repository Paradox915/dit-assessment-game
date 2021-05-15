# A star pathfinding
# Hugh Smith
'''
file for handling pathfinding
'''
# imports
import math

# functions

# get the distance between 2 points
def distance_between_points(point_1, point_2):
    '''
    @param : (int, int), (int, int)
    @throws : valueError
    @returns : float
    '''
    #   sqrt((x2-x1)^2+(y2-y1)^2)
    return math.sqrt(((point_2[0]-point_1[0])**2)+((point_2[1]-point_1[1])**2))

# the a star function
def a_star(grid_x, grid_y, obstacales, start, end):
    # postisions done like this in list
    # [(position),state , distance, steps, parent]

    # the main list
    grid = []
    # list of positions that are viable to search
    viable = []

    # loop through all values and append them to the lists
    for x in range(grid_x):
        for y in range(grid_y):
            # defulte varible values
            state = "na"
            distance = "na"
            parent = "na"
            steps = "na"
            # check if its is on the obstical list and if so them assing it as such
            if (x,y) in obstacales:
                state = "o"
            # check if its the starting postition
            elif (x,y) == start:
                state = "f"
                distance = distance_between_points(end, (x,y))
                steps = 0
                parent = "end"
                viable.append([(x,y),state,distance,steps, parent])
            # append the values to the main list 
            grid.append([(x,y),state,distance,steps, parent])

    # the grid in order based off postions so that we can get indexs if we have positions
    grid_pos = [item[0] for item in grid]

    # the main loop of the algorithem
    path_found = False
    while not path_found:
        # check if there is no possible path
        if len(viable) == 0:
            return "no possible path"
        # pick the postion in the viable that has the smallest distance to the end
        viable_distances = [item[2] for item in viable]
        # get the index of the item with the smallest distance
        viable_smallest = viable[viable_distances.index(min(viable_distances))]

        # get the index in the main grid
        viable_smallest_grid_index = grid_pos.index(viable_smallest[0])

        # uncover the area around it
        positions_to_check = [(1,0),(-1,0),(0,1),(0,-1)]
        for item in positions_to_check:

            # check if its in the list
            if (viable_smallest[0][0]+item[0],viable_smallest[0][1]+item[1]) in grid_pos:
                new_viable_index = grid_pos.index((viable_smallest[0][0]+item[0],viable_smallest[0][1]+item[1]))
                
                # check if its the obstical
                if grid[new_viable_index][1] != "o" and grid[new_viable_index][1] != "f"and grid[new_viable_index][1] != "d":
                    grid[new_viable_index][1] = "f"
                    grid[new_viable_index][2] = distance_between_points(end,grid[new_viable_index][0])
                    grid[new_viable_index][3] = viable_smallest[3] + 1
                    grid[new_viable_index][4] = viable_smallest_grid_index

                    viable.append(grid[new_viable_index])


        # delete the old value
        viable.remove(viable_smallest)
        grid[viable_smallest_grid_index][1] = "d"

        # check if path has been found 
        if end in [item[0] for item in viable]:
            path_found = True
    
    # get the path by following the trail of parent items
    path = []
    path_done = False
    viable_pos = [item[0] for item in viable]
    end_index =  grid_pos.index(end)
    path.append(grid[end_index][0])
    while not path_done:
        end_index = grid[end_index][4]
        # if at the end of the path
        if end_index == "end":
            path_done = True
        else:
            path.append(grid[end_index][0])

    return path
# main routine

# testing from the main file
if __name__ == "__main__":
    grid_x = 50
    grid_y = 50

    obstacales = [(2,2),(1,2),(0,2),(2,1)]
    print("the path is: ",a_star(grid_x, grid_y, obstacales,(1,1),(50000,50000)))
