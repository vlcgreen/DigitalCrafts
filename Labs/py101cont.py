# Continuation of Day 2 wrap up

# name = "victoria"

# a = 4

# b = 5

# a + 5
# #indentation is important in python, denotes conditional statement
# if True:
#     print("inside of condition")
# print("outside of our condition")

# age = int(input("How old are you >>")) #str => int

# if age >=21:
#     print("you get a free beer")
# elif age < 18:  #ELSE IF: adding another conditions
#     print("why are you even at a bar?")
# else:
#     print("You are not old enought to drink.")

# print("outside of our condition")

# name = input("What is your name?")

# count = 0

# while count < 10: 
#     print(f"The count is {count}")
#     count = count + 1 
# print("outside of our condition")

# answer = "" #when

# while answer != "when": 
#     answer = input('Say when: ')
#     answer = answer.lower() #WHEN, WhEn => when

# print('Cheese')

#BREAK AWAY STATEMENT REWRITTEN FROM ABOVE CODE:

while True:
    answer = input("Say when:  ")
    if answer.lower() == "when":
        break

print("cheese")

# #Divide check into equal amounts
# When True:
# service = input("How was your service (good, fair, or bad)? ")
#     if service.lower() == "good" or "fair" or "bad":
#         break


