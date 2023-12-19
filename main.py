if __name__ == "__main__":
    user_prompt ="type add or show or exit: "

    todos = [] # initialise an emppty list
    while True :
        user_action = input(user_prompt)

        match user_action:
            case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)
            case 'show':
                print(todos)   
            case 'exit':
                break    
print('Bye!')