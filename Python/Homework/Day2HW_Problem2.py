#Day 2 Homework Assignment


#PROBLEM 2

total_bill_amount = float(input("Your total bill >>  "))

#Find out how many ways to split check
total_party = int(input("How many people are splitting the check? "))

service_level = input("How was your service? \n1 - good, 2 - fair, or 3 - bad? ") 
#Need to define what tip amounts go to which service level next 
if service_level == '1':
    tip_amount = total_bill_amount * .2 
elif service_level == '2':
    tip_amount = total_bill_amount * .15
elif service_level == '3':
    tip_amount = total_bill_amount * .10
else:
    print("Please only input options 1, 2, or 3 for your quality of service")

before_split = final_bill = tip_amount + total_bill_amount
final_bill = (tip_amount + total_bill_amount) / total_party
print(f"Your tip amount: ${tip_amount} \nTotal Bill: ${before_split} \nAmount per person: ${final_bill} ")

#YAY!

