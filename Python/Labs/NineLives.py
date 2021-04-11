
import random

lives = 9
words = ['pizza', 'fairy', 'shirt', 'plane', 'javascript']

secret_word = random.choice(words)

print(secret_word)

clue = []
for stuff in secret_word:
    clue.append("_ ")
# clue = "_ "*len(secret_word)
# print(clue)
# print(secret_word.replace(secret_word, "_ "*len(secret_word)))

def update_clue(guessed_letter):
    index = 0
    # print(*clue, sep = " ")

    while index < len(secret_word):

        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1

# def check_win():
#     if "_ " not in clue:
#         print("You win")


while lives > 0:
    print(*clue, sep = " ") #to print it cleaner without brackets and commas
    if "_ " not in clue:
        print("\nYou win")
        break
    else:
        print(f"You have {lives} remaining")
    #show the num char need to guess
    #input a char
    
        guess = input("Guess a letter? ")

        if guess in secret_word:
            update_clue(guess)
        else:
            print("\nIncorrect. You lost a life")
            lives -= 1

print("\nGAME OVER.")

## Mess around with making the game into a giant loop later so it can replay. 
# replay = input("Play again? Y/N ")
# if y then replay, if no it breaks loop
# while replay.lowercase() == y:
        ## RE-TYPE GAME CODE
    ## replay = input("Play again? Y/N ")
