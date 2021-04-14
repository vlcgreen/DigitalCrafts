#Homework Problem 3 - Sorting a histogram

sentence = input("Please enter a sentence: ").lower()

words_dict = {}

sent_list = list(sentence)

split = []
word = ""
for letter in sentence:
    if letter == ' ':
        split.append(word)
        word = ""
    else:
        word += letter
if word:
    split.append(word)

for words in split:
    if words in words_dict:
        words_dict[words] += 1
    else:
        words_dict[words] = 1

# print(words_dict)
# for stuff in words_dict:
#     print(stuff)

top_val = []
sec_val = []
third_val = []
val = 0
for stuff in words_dict:
    if words_dict[stuff] > val:
        top_val = stuff, words_dict[stuff]
        val = words_dict[stuff]

#trying to do this without sorting or anything... will look again later. 
#this loop starts by giving me the values I need but it fails somewhere...