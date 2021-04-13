#going over homework probs

# for x in range(2):
#     for y in range(2):
#         print(f'[{x}][{y}]')

# m1 = [[1,3], [2,4]]
# m2 = [[5,2], [2,4]]
# final = []

# for a in range(0, 2):
#     m3 = []
#     for b in range(0, 2):
#         m3.append(m1[a][b] + m2[a][b])
        
#     final.append(m3)

# print(final)

# CAESAR CYPHER
#modulus
# alph = "abcdefghijklmnopqrstuvwxyz"
# shift = 13
# cypherbet = " "

# for char in alph:




#TO DO LIST:

# CRUD - create, read, update, delete

finished = 'y'
todoList = []
# add
def add():
    newTodo = input("Enter a new todo Item>> ")
    todoList.append(newTodo)
# displaying
def display():
    for index, todoItem in enumerate(todoList):
        print(f"{index + 1} {todoItem}")
# updating
def update(index, updatedValue):
    todoList[index] = updatedValue
# deleting
def delete():
    delnum = int(input("what do you want to delete?"))
    delindex = delnum - 1
    del todoList[delindex]
while finished == 'y':
    # menu
    print('what would you like to do?')
    userInput = input(f"""
1. List todos
2. Add a todo item
3. Delete a todo item
4. update a todo item
5. end the app                                 
""")
    choice = int(userInput)
    if choice == 1:
        display()
    elif choice == 2:
        add()
    elif choice == 3:
        delete()
    elif choice ==5:
        finished = 'n'
        