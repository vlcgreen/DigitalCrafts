#Functions Homework
# Problem 1: Find the smallest number

list1 = []

numbers = input("How many numbers do you want to enter?>> ")

i1 = 0
while i1 < numbers:
    entered = int(input("Please enter a number for your list: "))
    list1.append(entered)
    i1 += 1 

small = ""

index = 0
while index < len(list1):
    small = list1[index]
    if list1[index] < small:
        small = list1[index]
    index += 1 

print (small)

