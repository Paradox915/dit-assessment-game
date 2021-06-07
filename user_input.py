# user input
# Hugh Smith
'''
file for handling user input
'''
# functions
# get movement input
def movement_input(user_input , keys = ["w","s","a","d"]):
    '''
    @param : string
    @returns : (int,int)
    @throws : 
    '''
    # check if input is valid
    if user_input in keys:
        # get the index of the input
        user_index = keys.index(user_input)
        # return a direction based of the index of the input
        if user_index == 0:
            return (0,-1)
        elif user_index == 1:
            return (0,1)
        elif user_index == 2:
            return (-1,0)
        else:
            return (1,0)
    return (0,0)


# main routine
# testing
if __name__ == "__main__":
    print(movement_input("d"))