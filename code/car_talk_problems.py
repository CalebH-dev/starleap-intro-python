
print("Problem 1:")

def if_3_repeating_letters(word):
    word = word.strip()
    if len(word) < 6:
        return False
    
    repeated_letters = 0
    index = 1
    last_letter = word[index -1]

    while index < (len(word) - 1):
        last_letter = word[index - 1]
        # print(f"Index: {index}. Current: {last_letter}. Next: {word[index]}. Repeat: {repeated_letters}")

        if word[index] == last_letter:
            repeated_letters +=1
            index += 2
             
        else:
            index +=1
            repeated_letters = 0

        if repeated_letters >= 3:
            return True
            
    return False



file_name = '../shared/words.txt'
file = open(file_name)

print(f"Looking for a word with 3 sets of consecutive double characters in: {file_name}")

num = 0


for line in file:
    
    num += 1
    
    is_looking_for = if_3_repeating_letters(line)

    if is_looking_for:
        print(f"Word is {line.strip()}")
        # print(f"Line number {num}")





print("Problem 2:")

"""I was driving on the highway the other day and I happened to notice my odometer. 
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles, 
for example, I'd see 3-0-0-0-0-0.
Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic; 
that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my 
odometer could have read 3-1-5-4-4-5.
One mile later, the last 5 numbers were palindromic. For example, it could have read 
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. 
One mile later, all 6 were palindromic!

The question is, what was on the odometer when I first looked?"""

def is_palindrome(n): 
    
    s = str(n)

    end = len(s) - 1
    start = 0
    


    while start < len(s)/2:
        if s[start] == s[end]:
            start +=1
            end -=1
        else:
            return False
    
    return True

def last_x_char(n, x):
    s = str(n)
    return s[len(s) - x:]



for num in range(100000, 999999):
    plus = 1

    if is_palindrome(last_x_char(num, 4)):

        if is_palindrome(last_x_char(num+1, 5)):

            if is_palindrome(last_x_char(num+2, 5)[:-1]):
                # print(f"Condition 3: {num+2}")

                if(is_palindrome(num+3)):
                    print(f"solution: {num}")

    



