
rock = ['rock', 'r']
paper = ['paper', 'p']
scissors = ['scissors', 's', 'scizzorz']

def is_valid_input(text):
    text = text.lower()
    if(text in rock):
        return 1
    if(text in paper):
        return 2
    if(text in scissors):
        return 3
    return 0
    
count = 0


while 1:
    print("Rock, Paper, Scizzorz!!!\n\n")
    
    p1 = is_valid_input(input("Player 1: "))
                        
    while (p1 == 0):
        print("Player 1 try again\n")
        p1 = is_valid_input(input("Player 1: "))

    p2 = is_valid_input(input("Player 2: "))

    while (p2 == 0):
        print("Player 2 try again\n")
        p2 = is_valid_input(input("Player 2: "))

    print()
    if((p1 == 3) and (p2 == 1)):
        print("Player 1 Wins!!!\n\n")
    elif(p1 > p2):
        print("Player 1 Wins!!!\n\n")
    elif(p1 == p2):
        print("Nobody Wins!!!\n\n")
    else:
        print("Player 2 Wins!!!\n\n")

    count += 1

    if(count>3):
        print("Muwahahaha!!! Infinite loop!")
    

    