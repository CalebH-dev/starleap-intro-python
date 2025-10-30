
import string


# def play_nims(pile, max_stones):
#     '''
#     An interactive two-person game; also known as Stones.
#     @param pile: the number of stones in the pile to start
#     @param max_stones: the maximum number of stones you can take on one turn
#     '''

    ## Basic structure of program (feel free to alter as you please):

def get_user_input(max_val, max_attempts, player):
    
    in_string = f"""Player {player}: How many stones to get? """

    while(max_attempts > 0):
        usr_in = input(in_string)

        if(usr_in.isdigit()):
            usr_in = int(usr_in)

            if(usr_in > 0 and usr_in <=max_val):
                return usr_in
            else:
                in_string = f"""Player {player}: must be < {max_attempts} and > 0 """
            
        else:
            max_attempts += 1
            in_string = f"""Player {player}: try again """

    return -1            

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over.  Player __ is the winner!"

stones = 100


while(stones > 0):
    stones -= get_user_input(5, 5, 1)
    print("There are ", stones, " left")
    if(stones <= 0):
        print("Player 1 wins")
        break
    stones -= get_user_input(5, 5, 2)
    if(stones <= 0):
        print("Player 2 wins")
        break
    print("There are ", stones, " left")

