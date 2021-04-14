#Homework Problem 2: Word Summary

# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# $ python3 word_histogram.py
# Please enter a sentence: To be or not to be
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}

# sentence = input('Please enter a sentence: ')

sentence = input("Please enter a sentence: ").lower()

words_dict = {}

sent_list = list(sentence)
# print(testlist)

split = []
word = ""
for letter in sentence:
    if letter == ' ':
        split.append(word)
        word = ""
    if letter == ".":
        pass
    else:
        word += letter
if word:
    split.append(word)

for words in split:
    if words in words_dict:
        words_dict[words] += 1
    else:
        words_dict[words] = 1

print(words_dict)