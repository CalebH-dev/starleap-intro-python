


fin = '../shared/words.txt'

f = open(fin)

words = list()
line = ' \n'

while len(line) > 0:
    line = f.readline()
    line = line.strip()
    words.append(line)

words = tuple(words)


def forbiden_letters(w, l):

    legal_words_count = 0
    
    for word in w:
        if l in word:
            pass

        else:
            legal_words_count +=1

    f.close()

    return legal_words_count



alpha = list()
for n in range(ord('a'), ord('z')+1):
    alpha.append(chr(n))

alpha = tuple(alpha)

words_without_letter = list()

i = 0
for l in alpha:
    words_without_letter.append(forbiden_letters(words, l))


for n in range(len(alpha)):
    print(f"{words_without_letter[n]} words that do not contain {alpha[n]}")




# file = open('../shared/words.txt')

# is_greater_20 = 0

# longest_word = '0'
# longest_word_size = 0

# for line2 in file:
#     if len(line2) >= 20:
#         is_greater_20 +=1
#         print(line2)
    
#     if len(line2) > longest_word_size:
#         longest_word = line2.strip()
#         longest_word_size = len(longest_word)
# eater_20 = 0

# longest_word = '0'
# longest_word_size = 0

# for lines in file:
#     if len(lines) >= 20:
#         is_greater_20 +=1
#         print(lines)
    
#     if len(lines) > longest_word_size:
#         longest_word = lines.strip()
#         longest_word_size = len(longest_word)


letter = forbiden_letters(words, 'e')


# # print(f"{num} words total")

# print(f"{is_greater_20} words are greater than 20 characters")

print(f"{letter} words do not contain 'e', {len(words)} words total")

# print(f"{longest_word} is the largest word. It is {longest_word_size} characters")


