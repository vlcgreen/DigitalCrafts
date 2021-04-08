#Day 2 Homework Assignment

# PROBLEM 6 - MULTIPLICATION TABLE


row = 0

for line in range (1, 11):
    while row < 10:
        num2 = row
        row += 1
        for num1 in range (1, 11):
            print(f"{row} x {num1} = {row*num1} ")



