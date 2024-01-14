if __name__ == "__main__":
    user_prompt ="type add or show, edit, complete or exit: "

    while True:
        user_action = input(user_prompt)
        user_action = user_action.strip() # removes whitespace

        if user_action.startswith("add"):
            todo = user_action[4:] #list slice from just after "add "

            with open('todos.txt','r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                file.writelines(todos)     

        elif user_action.startswith("show"): #startswith is a string function
            with open('todos.txt','r') as file:
                todos = file.readlines()
                new_todos = [item.strip('\n') for item in todos] # list compehension
            for index,item in enumerate(new_todos): 
                item = item.title()
                row = f"{index + 1}. {item}"
                print(row) 

        elif user_action.startswith("exit"):
            break     

        elif user_action.startswith('complete'):
            try:
                with open('todos.txt','r') as file:
                    todos = file.readlines()

                number = int(user_action[9:])
                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
                
                message = f"Todo {todo_to_remove} was removed"
                print(message)
            except IndexError:
                print('There is no item with that index')
                continue

        elif user_action.startswith('edit'):
            try:
                with open('todos.txt', 'r') as file:
                    todos = file.readlines()

                number = int(user_action[5:]) -1

                existing_todo = todos[number] 
                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo +'\n'

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
            except ValueError:
                print('Command is not valid')
                continue #forces the code into a new run of the while loop

        else:
            print("Command is not valid")

print('Bye!')