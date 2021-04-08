#Day 2 Homework Assignment

# PROBLEM 3 - HOW MANY COINS?

coins = 0

while True:
    print(f"\nYou currently have {coins}coins.")
    answer = input("\nDo you want another? Y/N >> ")
    if answer.lower() == 'y':
        coins += 1
    elif answer.lower() == 'n':
        print("\nBye!")
        break
    else:
        print("\nYou need to enter Y/N.")
        continue

