import string

var1 = "hi"
var2 = "hello"
var3 = "Hello World several hundred times to make a very super long string that is longer than 70 but I doubled it in length to make it even longer than an insainly huge number! But nevertheless, thisstringisstillnotlongenoghorrepresentativeofallstrings so I continue to ramble in order to get more length."

def right_justify(input, lin_len, count = 1):

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
        right_justify(string2, lin_len, count + 1)

    # print("recursion depth: " + str(count))

  



right_justify(var3, 50)

print("Break")

x = var3.split(" ")
print(x)
