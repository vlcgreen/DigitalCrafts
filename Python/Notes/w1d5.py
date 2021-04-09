#Friday Notes: Functions

# def separateRuns():
#     print("******************")
#     print()

# def getGroceries(i1, i2,i3,i4):
#     print(i1)
#     print(i2)
#     print(i3)
#     print(i4)
#     separateRuns()

# getGroceries("milk", "beer", "tacos", "Monster Energy")

# def getChores():
#     print("laundry")
#     print("vacuum")
#     separateRuns()

# getGroceries() #calling function
# getChores() 

# foo = 1

# def myFunc(myParameter):
#     print(myParameter)

# def add(num1, num2): #in parenthesis are the parameters!
#     return num1 + num2

# result = add(2, 3) #here in parenthesis are the arguments!
# print(result)


# def make_formal_greeting(name, title):
#     return f"This is {name}, the {title}!"

# result = make_formal_greeting("Jason", "Red Ranger")

# oops = make_formal_greeting("Red Ranger", "Jason")

# print(result)
# print(oops)

# def blend(setting, time):
#     return f"Blend on {setting} for {time} minutes"

# print(blend('high', 10))

#Building a simple func that does addition

# def addTwo(startingValue):
#     endingValue = startingValue + 2
#     print('The sum of', startingValue, 'and 2 is:', endingValue)

# # Call the function twice with different arguments
# result = addTwo(5)
# addTwo(10)
# print(result)

##Building a function to Calculate an Average

# def calculateAverage(param1, param2, param3, param4):
#     # Add up numbers, divide by the number of numbers
#     total = param1 + param2 + param3 + param4
#     average = total / 4.0
# #     print('Average value is:', average)
# calculateAverage(2, 3, 4, 5)
# calculateAverage(-3, 5.2, 15, 1000.8)
# calculateAverage(1.4, -2.5, 14.3, 200.5)

# firstName = input("What is your first name? ")
# lastName = input("What is your last name? ")

# def greeting(fName, lName):
#     print(f'{fName} {lName}')

# greeting(firstName, lastName)

# def add(num1, num2): 
#     print(num1 + num2)
#     return num1 + num2

# result = add(4,5)
# print(result)

# mult = 3 * result


# def dance():
#     kind = "jazz"
#     print(f"I am doing a {kind} dance")
#     return

# result = dance()

# print(result)

# ( num * (num1 + num2) ) / num
# def add(num1, num2):
#     return num1 + num2

# def mult(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1/num2

# # 7 * (6 + 5)

# addnum = add(6, 5)

# print(div(mult(7,addnum), 4))

