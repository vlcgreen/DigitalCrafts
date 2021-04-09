
import random

lives = 9
words = ['pizza', 'fairy', 'shirt', 'plane', 'javascript']

secret_word = random.choice(words)

print(secret_word)

clue = []
for stuff in secret_word:
    clue.append("_ "*len(secret_word))
# clue = "_ "*len(secret_word)
# print(clue)
# print(secret_word.replace(secret_word, "_ "*len(secret_word)))

def update_clue(guessed_letter):
    index = 0
    while index < len(secret_word):

        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            index += 1

while lives > 0:
    print(clue)
    print(f"You have {lives} remaining")
    #show the num char need to guess
    #input a char
    guess = input("Guess a letter? ")
    
    if guess in secret_word:
        update_clue(guess)
    else:
        print("Incorrect. You lost a life")
        lives -= 1


