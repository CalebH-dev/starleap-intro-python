
# Sqrt aproximation
# a = int(input("input value to find sqrt of: "))
# x = int(input("Esitmate sqrt value: "))

# oldval = x
# newval = 0
# while(1):

#     newval = (oldval + a/oldval) / 2
#     print("New estimate: ", newval)
#     if oldval == newval:
#         break

#     oldval = newval

# Print string backwards
# index = 0
# fruit = 'qwertyuiop'
# while index < len(fruit):
#     tmp = index + 1
#     # if index == 0:
#     #     tmp = 1
#     letter = fruit[-tmp]
#     print(letter)
#     index = index + 1

word1 = 'mots'
word2 = 'stop'


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)

    while j > 0:
        # print(i, " ", j)
        # print(word1[i], " ", word2[j - 1])
        
        if word1[i] != word2[j - 1]:
            return False
        i = i+1
        j = j-1

    return True

if is_reverse(word1, word2):
    print("reversed")

else: 
    print("not reversed")