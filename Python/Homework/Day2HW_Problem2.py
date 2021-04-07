#Day 2 Homework Assignment


#PROBLEM 2 TIP CALCULATOR 2

while True:
    try:
        total_bill_amount = float(input("\nYour total bill >>  "))
        break
    except ValueError:
        print("\nPlease only enter numbers")
print(total_bill_amount)

#Find out how many ways to split check
# total_party = int(input("How many people are splitting the check? "))
while True:
    try:
        total_party = int(input("\nHow many people are splitting the check? "))
        break
    except ValueError:
        print("\nPlease only enter whole numbers")
print(total_party)

#Requesting input for service level
while service_level != '1' or '2' or '3':
    print("\nPlease only input options 1, 2, or 3 for your quality of service")
    service_level = input("\nHow was your service? \n1 - good, 2 - fair, or 3 - bad? ")
    if service_level == '1' or '2'or '3':
        break

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
print(f"\nTip amount: ${tip_amount} \nTotal Bill: ${before_split} \nAmount per person: ${final_bill} ")

#YAY!

