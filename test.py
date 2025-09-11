import string

var1 = "hi"
var2 = "hello"
var3 = "Hello World several hundred times to make a very super long string that is longer than 70"

def right_justify(input):

    index = [0, 0, 0]
     
    buffer = [" ", " "]
    index[0] = input.rfind(" ", 0, 70)
    buffer[0] = input[:index[0]]
    buffer[1] = input[index[0]:]
    buffer[0]
    print(buffer[0])
    print(buffer[1])
    
    
    
    # number = input.count(" ")
    # index = input.find(" ")

    # print(index)
    # if((index != -1) and (len(input) > 70)):
    #     buffer[0] = input[index:]
    #     buffer[1] = input[:index]
    #     print(buffer)
        
    # if index < 70 and len(input) > 70:
    #     buffer[0] = input[index:]
    #     buffer[1] = input[:index]
    #     print(buffer)
        
            


    # print(" " * (70 - len(input)) + input)

# right_justify(var1)
# right_justify(var2)
right_justify(var3)



