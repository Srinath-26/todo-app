#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()
    if user_action.startswith('add'):
        with open('todos.txt', 'a') as file:
            todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            number = number - 1

            print("Here is todos existing", todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos("todos.txt", todos)

        except (IndexError, ValueError) as error:
            match error:
                case IndexError():
                    print("You are trying to edit an item that does not exist")

                case ValueError():
                    print("You did not enter a number. Pleas enter the number of the item you want to edit")

            continue



    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            number = number - 1

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos("todos.txt", todos)

            message = f"Todo, '{todo_to_remove}' has been completed and removed from the list"
            print(message)


        except (IndexError, ValueError) as error:

            match error:

                case IndexError():

                    print("You are trying to complete an item that does not exist")

                case ValueError():

                    print("You did not enter a number. Pleas enter the number of the item you want to edit")

            continue



    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")
        


print("Bye!")
