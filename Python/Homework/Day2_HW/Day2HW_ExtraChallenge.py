#Day 2 Homework Extra Challenge

# PROBLEM 1 - TRIANGLE NUMBERS
## Print the first 100 triangle numbers. formula

# num = 0 

# for numbers in range(1,100):
#     num += numbers
#     print (num)

#I worked it this way first but it wasn't as pretty:
for stuff in range(1,100):
    f = stuff * (stuff + 1) / 2
    print(int(f))

#PROBLEM 2 - FACTOR A NUMBER

factor = input("What number would you like to factor?>> ")

while type(factor) != int:
    print('Please enter whole numbers only')
    factor = input("What number would you like to factor?>> ")
    if type(factor) == int:
        break
    break

#I'm stuck from here, will look at how to factor it later