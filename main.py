if __name__=="__main__":

    from modules import functions
    import time

    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(f"It is {now}")
    
    user_prompt ="type add or show, edit, complete or exit: "
    while True:
        user_action = input(user_prompt)
        user_action = user_action.strip() # removes whitespace

        if user_action.startswith("add"):
            todo = user_action[4:] #list slice from just after "add "

            todos = functions.get_todos()
            todos.append(todo + '\n')
        
            functions.write_todos(todos)

        elif user_action.startswith("show"): #startswith is a string function
            todos = functions.get_todos()
            new_todos = [item.strip('\n') for item in todos] # list compehension
            for index,item in enumerate(new_todos): 
                item = item.title()
                row = f"{index + 1}. {item}"
                print(row) 

        elif user_action.startswith("exit"):
            break     

        elif user_action.startswith('complete'):
            try:
                todos = functions.get_todos()

                number = int(user_action[9:])
                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                functions.write_todos(todos)
                
                message = f"Todo {todo_to_remove} was removed"
                print(message)
            except IndexError:
                print('There is no item with that index')
                continue

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:]) -1

                todos = functions.get_todos()
                existing_todo = todos[number] 
                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo +'\n'

                functions.write_todos(todos)
                
            except ValueError:
                print('Command is not valid')
                continue #forces the code into a new run of the while loop

        else:
            print("Command is not valid")

print('Bye!')