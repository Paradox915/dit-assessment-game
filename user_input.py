# user input
# Hugh Smith
'''
file for handling user input
'''
# functions
# get movement input
def movement_input(keys = ["w","s","a","d"], text = " "):
    '''
    @param : [string]
    @returns : string
    @throws : 
    '''
    # loop untill a valid input is gotten
    getting_input = True
    while getting_input:
        # get the input
        user_input = input(text).lower()
        # check if input is valid
        if user_input in keys:
            # if so then exit the while loop
            getting_input = False
    # get the index of the input
    user_index = keys.index(user_input)
    # return a direction based of the index of the input
    if user_index == 0:
        return "up"
    elif user_index == 1:
        return "down"
    elif user_index == 2:
        return "left"
    else:
        return "right"


# function to get input of specifyed type
def get_input(check_type = int, question = "? ", wrong_type = "wrong type"):
    '''
    @param : type
    @returns : input of given type
    @throws : not valid type
    '''
    # loop untill a valid input is entered
    got_input = False
    while not got_input:
        try: 
            user_input = check_type(input(question))
            got_input = True
        # if input is of wrong type
        except ValueError:
            print(wrong_type)
    return user_input


# main routine
# testing
if __name__ == "__main__":
    print(movement_input())
    print(get_input())