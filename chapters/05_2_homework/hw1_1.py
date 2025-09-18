
##### Template for Homework 1, Exercises 1-3 ######


print("********** Homework 1 Exercise 1 **********")

def print_grid(h, w):

    line_char2 = "  |" * (w-1)
    print(line_char2)
    line = 0
    for line in range(h):
        if(line < h and line >= 0):
            if(line % 2 == 0):
                line_char1 = "----" * w
                print(line_char1)
            elif(line % 2 == 1):
                line_char2 = "   |" * (w-1)
                print(line_char2)
        line += 1


    line_char2 = "  |" * (w-1)
    print(line_char2)


Hight = input("Hight of tic-tac-toe: ")
print(Hight)
Width = input("Width of tic-tac-toe: ")
print(Width)

print_grid(int(Hight), int(Width))



print("********** Homework 1 Exercise 2 **********")

# Do your work for Excercise 2 here

print("Homework 1 Exercise 2: Not implemented") # Delete this line when you write your code!



print("********** Homework 1 Exercise 3 **********")

# Do your work for Excercise 3 here

print("Homework 1 Exercise 3: Not implemented") # Delete this line when you write your code!
