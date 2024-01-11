if __name__ == "__main__":
    user_prompt ="type add or show, edit, complete or exit: "

    while True :
        user_action = input(user_prompt)
        user_action = user_action.strip() # removes whitespace
        match user_action:
            case 'add':
                todo = input("Enter a todo: ") + "\n"

                with open('todos.txt','r') as file:
                    todos = file.readlines()

                todos.append(todo)

                with open('todos.txt', w) as file:
                    file.writelines('todos.txt')
                            
            case 'show' : 
                with open('todos.txt','r') as file:
                    todos = file.readlines()

                new_todos = [item.strip('\n') for item in todos] # list compehension
                
                for index,item in enumerate(new_todos): 
                    item = item.title()
                    row = f"{index + 1}. {item}"
                    print(row) 
            case 'exit':
                break
            case 'complete':
                number = int(input("Number of the todo to complete: "))-1
                todos.pop(number)
            case 'edit':
                for index,item in enumerate(todos): 
                    row = f"{index}. {item}"
                    print(row)  
                number = int(input("Number of the todo to edit: "))-1
                existing_todo = todos[number] 
                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo
print('Bye!')