# Lists

# arr = [ [1, 2], [3, 4], [4, 5], [7, 8] ]

# print(arr[3][0])

# board = [ ["X", "X", "O"], 
#           ["X", "O", "O"], 
#           ["X", "", "O"]
#         ]

# greeting = "Hello World"
# greeting[1] #e
# print(len(greeting))
# print(greeting[5:])

# greet = ['h', 'e', 'l', 'l', 'o']
# greet[1] #e

# len(greet)


alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = 0

# while index <= len(alphabet)-1:
#     print(alphabet[index])
#     index += 1
# print(alphabet)

# alphList = list(alphabet) #convert string to list

# print(alphList)
# #now you can change elements just like a real list 
# alphList [1] = "z"
# print(alphList)

# alphStr = "".join(alphList)
# print(alphStr)

# alphStr = " * ".join(alphList)
# print(alphStr)

# constants = (3.14, 2.71) #tuple

# # constants[0] = 3 #cannot change tuples not mutable
# print(constants[0])

# s = 5
# myList = range(10, 50, 2*s) #third number shows steps between number can be played with

# print(list(myList))

# name = "Victoria"

# for c in name:
#     print(c)

# sum = 0
# arr = [4, 2, 5, 7, 23, 6, 5]

# for val in arr:
#     sum = sum + val
# print(sum)

#Finding largest number
# arr = [4, 2, 5, 7, 23, 6, 5]

# check = 0
# for num in arr:
#     if check < num:
#         check = num

# print(check)

#Finding even number
# arr = [4, 2, 5, 7, 23, 6, 5]

# check = []

# for num in arr:
#     if num % 2 == 0:
#         check.append(num)

# print(check)


#given a string, print the string reversed

# name = "VICTORIA"
# ind = 7
# count = name[ind]
# reverse = []
# for i in name:
#     count = name[ind]
#     reverse.append(count)
#     ind-=1
# print (reverse)

##Printing reverse of a neg number
num = -9854
sign = -1
sn = str(abs(num))
rev_num = ""

for n in sn:
    rev_num = n + rev_num
rev_num = int(rev_num)
if num < 0 :
    print (rev_num*sign)
else:
    print(rev_num)

