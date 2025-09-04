
##### Template for Chapter 3.14, Exercises 1 - 3 ######

# Do your work for Exercise 1 here

print("********** Ch 3 Exercise 1 **********")
print()
print()

import string

var1 = "hi"
var2 = "hello"
var3 = "fhadhbvidfvdfgdfsfdfdfgbwjevhfdbfjfv fdagsdffgsdfgrndnrdgrnmasdfasfdjkcaeiufhbusvedbvnkjvfjd"

def right_justify(input):

     
    buffer[0] = ""
    counter = 0
    number = input.count(" ")
    index = input.find(" ")

    print(index)
    if((index != -1) and (len(input) > 70)):
        if index > 70:
            buffer[0] = input[index:]
            buffer[0] = input[:index]
            


    print(" " * (70 - len(input)) + input)

right_justify(var1)
right_justify(var2)
right_justify(var3)





print("********** Ch 3 Exercise 2 **********")

# Do your work for Excercise 2 here.

print("Ch 3 Exercise 2: Not implemented") # Delete this line when you write your code!



print("********** Ch 3 Exercise 3 **********")

# Do your work for Exercise 3 here.

print("Ch 3 Exercise 3: Not implemented") # Delete this line when you write your code!
