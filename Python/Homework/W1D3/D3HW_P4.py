# Homework Problem 4

list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '8', '7', '2', '1', '1', '5', '4']

list2 = []

for x in list1:
    if x not in list2:
        list2.append(x)
        
print(list2)