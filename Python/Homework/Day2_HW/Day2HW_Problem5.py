#Day 2 Homework Assignment

# PROBLEM 5 - PRINT A TRIANGLE

# Math for pyramids: each row number(a) has (b)stars, where b = 2a-1

row = 0

while row < 5:
    row += 1
    spaces = 5 - row

    even = 0
    while even < spaces:
        print (" ", end='')
        even +=1

    stars = 2*row-1
    while stars > 0:
        print("*", end="")
        stars -= 1

    print()
