#Homework Problem 1:

#Letter Summary

# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# $ python3 letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

word = input("Please enter a word: ")

word_dict = {}

for letter in word:
    if letter in word_dict:
        word_dict[letter] += 1
    else:
        word_dict[letter] = 1

print(word_dict)