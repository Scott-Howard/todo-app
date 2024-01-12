if __name__ == "__main__":
    user_prompt ="type add or show, edit, complete or exit: "

    while True:
        user_action = input(user_prompt)
        user_action = user_action.strip() # removes whitespace


        if 'add' in user_action:
            todo = user_action[4:] #list slice from just after "add "

            with open('todos.txt','r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                        
        elif 'show' in user_action: 
            with open('todos.txt','r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos] # list compehension
            
            for index,item in enumerate(new_todos): 
                item = item.title()
                row = f"{index + 1}. {item}"
                print(row) 
        elif 'exit' in user_action:
            break
        
        elif 'complete' in user_action:
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
                
        elif 'edit'in user_action:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(user_action[5:]) -1

            existing_todo = todos[number] 
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo +'\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        else:
            print("Command is not valid")



print('Bye!')