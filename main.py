if __name__ == "__main__":
    user_prompt ="type add or show or exit: "

    todos = [] # initialise an emppty list
    while True :
        user_action = input(user_prompt)
        user_action = user_action.strip() #removes whitespace
        match user_action:
            case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)
            case 'show':
                #print(todos)
                for item in todos: #nicely prints out the contents of todo
                    print(item)   
            case 'exit':
                break
            case _: #underscore _ is a convention for this part of code for the uninitialse variable
                print("Enter a known command")    
print('Bye!')