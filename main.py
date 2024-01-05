if __name__ == "__main__":
    user_prompt ="type add or show, edit, complete or exit: "

    todos = [] # initialise an emppty list
    while True :
        user_action = input(user_prompt)
        user_action = user_action.strip() #removes whitespace
        match user_action:
            case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)
            case 'show' : 
                #print(todos)
                for index,item in enumerate(todos): #nicely prints out the contents of todo
                    item = item.title()
                    row = f"{index + 1}. {item}"
                    print(row) 
            case 'exit':
                break
            case 'complete':
                number = int(input("Number of the todo to complete: "))-1
                todos.pop(number)
            case 'edit':
                for index,item in enumerate(todos): #nicely prints out the contents of todo
                    row = f"{index}. {item}"
                    print(row)  
                number = int(input("Number of the todo to edit: "))-1
                existing_todo = todos[number] 
                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo
print('Bye!')