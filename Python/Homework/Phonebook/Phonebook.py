#Working on phonebook

import pickle

# with open('phonebook.pickle', 'wb') as fh:
#     pickle.dump(phonebook_dict, fh)

with open('phonebook.pickle', 'rb') as fh:
    phonebook_dict = pickle.load(fh)

#1. Look up an entry
def LookUp(name):
    print(f"\nFound entry for {name}: {phonebook_dict[name]}")
#2. Set an entry
def entry():
    entry_name = input("\nWhat name do you want to enter? ")
    entry_phone = input("What is their number? \n(Please format XXX-XXX-XXXX) >> ")
    phonebook_dict[entry_name] = entry_phone
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(phonebook_dict, fh)
    print(f"Entry stored for: {phonebook_dict[entry_name]}")

#3. Delete an entry
def delete(name):
    del phonebook_dict[name]
    print(f"You have deleted the entry for {name}")

#4. List all entries
def all_entries():
    # print(phonebook_dict)
    print("\n\nThe following are found entries in the phonebook:\n")
    for x in phonebook_dict:
        print(f"{x}: {phonebook_dict[x]}")

# Ask user for input 
## What do you want to do 1-5?
action = " "
while action != '1' or '2' or '3' or '4' or '5':
        print('''
        Electronic Phone Book
        ======================
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Quit
        ''')
        action = input("\nWhat Would you like to do (1-5)?")

        if action == '1':
            name = input("\nWho would you like to look up? ")
            LookUp(name)
        if action == '2':
            entry()
        if action == '3':
            name = input("\nWho would you like to delete? ")
            delete(name)
        if action == '4':
            all_entries()
        if action == '5':
            print("\nBye.")
            break

