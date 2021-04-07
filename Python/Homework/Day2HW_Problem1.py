#Day 2 Homework Assignment

# PROBLEM 1. TIP CALCULATOR


# This is to get the input for the total bill
# total_bill_amount = float(input("Your total bill >>  "))
# Verifying they put the correct type of data
while True:
    try:
        total_bill_amount = float(input("Your total bill >>  "))
        break
    except ValueError:
        print("Please only enter numbers")
print(total_bill_amount)


#Find out how service was to define service tip amount to be used
service_level = input("How was your service? \n1 - good, 2 - fair, or 3 - bad? ")
#Trying to get the correct input from user
while service_level != '1' or '2' or '3':
    print("Please only input options 1, 2, or 3 for your quality of service")
    service_level = input("How was your service? \n1 - good, 2 - fair, or 3 - bad? ")
    if service_level == '1' or '2'or '3':
        break

#Calculating based on service level answer
if service_level == '1':
    tip_amount = total_bill_amount * .2 
    final_bill = tip_amount + total_bill_amount
    print(f"Your tip amount: ${tip_amount} /nYour total amount: ${final_bill} ")
elif service_level == '2':
    tip_amount = total_bill_amount * .15
    final_bill  = tip_amount + total_bill_amount
    print(f"Your tip amount: ${tip_amount} /nYour total amount: ${final_bill} ")
elif service_level == '3':
    tip_amount = total_bill_amount * .10
    final_bill  = tip_amount + total_bill_amount
    print(f"Your tip amount: ${tip_amount} /nYour total amount: ${final_bill} ")
# else:
#     print("Please only input options 1, 2, or 3 for your quality of service")

