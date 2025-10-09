def del_nl(buff):
    index = 0
    input = buff
    done = 0
    while(index < len(input) and done == 0):
        if(input[index] == ("\n" or "\r")):
            input = input[:index] + input[(index + 1):]
        
        index += 1
        if(input.find("\n") == -1):
            done = 1

    return input

file_name = input("Enter file name to open: ")
f = open("text.txt", "r")
buff = del_nl(f.read())
f.close()

# print(buff)
f = open("text.txt", "w")
f.write(buff)
f.close()

print("Removed new line characters from " + file_name)