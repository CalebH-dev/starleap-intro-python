


fin = open('../shared/words.txt')

line = "1"
count_of_e = 0
num = 0

while len(line) > 0:

    line = fin.readline()
    if "e" in line:
        pass

    else:
        out = line.strip()
        # print(out)
        count_of_e +=1
    num +=1



file = open('../shared/words.txt')

is_greater_20 = 0

longest_word = '0'
longest_word_size = 0

for line2 in file:
    if len(line2) >= 20:
        is_greater_20 +=1
        print(line2)
    
    if len(line2) > longest_word_size:
        longest_word = line2.strip()
        longest_word_size = len(longest_word)
eater_20 = 0

longest_word = '0'
longest_word_size = 0

for lines in file:
    if len(lines) >= 20:
        is_greater_20 +=1
        print(lines)
    
    if len(lines) > longest_word_size:
        longest_word = lines.strip()
        longest_word_size = len(longest_word)







print(f"{num} words total")

print(f"{is_greater_20} words are greater than 20 characters")

print(f"{count_of_e} words do not contain 'e', {num} words total")

print(f"{longest_word} is the largest word. It is {longest_word_size} characters")


