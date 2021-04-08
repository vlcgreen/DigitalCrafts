#Day 2 Homework Assignment

# PROBLEM 4 - PRINT A BOX

width = int(input("Width? "))
height = int(input("Height? "))
print("*"*width)

for i in range (height-2):
    print("*"+" "*(width-2)+"*")
print("*"*width)
