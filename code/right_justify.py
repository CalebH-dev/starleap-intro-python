import string

var1 = "hi"
var2 = "hello"
var3 = "Hello World several hundred times to make a very super long string \
    that is longer than 70 but I doubled it in length to make it even longer than an \
    insainly huge number! But nevertheless, thisstringisstillnotlongenoghorrepresentativeofallstrings \
    so I continue to ramble in order to get more length."

def right_justify_recursive(input, lin_len, count = 1):

    # lin_len = 50
    # print("recursion depth: " + str(count))

    # if input is small, don't break it, otherwise find a space to break
    if(len(input) < lin_len):
        index = lin_len
    else:
        index = input.rfind(" ", 0, lin_len) 
        if(index <= 0):
            index = lin_len

    if((count != 1) and (input.find(" ") == 0)):
        input = input[1:]

    string1 = input[:index]

    # if(len(input) < (lin_len * count + 1)):
    string2 = input[index:]
    # else:
    #     string2 = input[index:]

   
    if(len(string1) > lin_len):
        tempstr = string1[:lin_len]
        string1 = string1[lin_len:]
        string2 += tempstr
       
    print(string1)

    if(len(string2) > 0):
        right_justify_recursive(string2, lin_len, count + 1)

    # print("recursion depth: " + str(count))




def right_justify_loop(buff, lin_len, count = 1):

    input = buff
    # if input is small, don't break it, otherwise find a space to break

    if(lin_len < 2):
        lin_len = 50
        print("Max line length is to samll. Using default (50)\n\n")

    while(count == 1 or len(input) > lin_len):
        
        if(len(input) < lin_len):
            index = lin_len
        else:
            index = input.rfind(" ", 0, lin_len) 
            if(index <= 0):
                index = lin_len

        if((count != 1) and (input.find(" ") == 0)):
            input = input[1:]

        string1 = input[:index]
        input = input[index:]
    
        if(len(string1) > lin_len):
            tempstr = string1[:lin_len]
            string1 = string1[lin_len:]
            input += tempstr
        
        print(string1)

        count+= 1

    if(len(input) > 0):
        if(input[0] == " "):
            input = input[1:]
        print(input)


# For parsing a file
# size = input("Enter max line length: ")
# file = input("Enter file to justify: ")
# size = int(size)
# f = open(file)
# file_contense = f.read()
# right_justify_loop(file_contense, size)
right_justify_loop(var3, 50)
