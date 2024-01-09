if __name__ == "__main__":
    user_prompt ="type add or show, edit, complete or exit: "

    while True :
        user_action = input(user_prompt)
        user_action = user_action.strip() #removes whitespace
        match user_action:
            case 'add':
                todo = input("Enter a todo: ") + "\n"

                file = open('todos.txt','r')
                todos = file.readlines()
                file.close()

                todos.append(todo)
                file = open('todos.txt', 'w')
                file.writelines(todos)
                file.close()
            case 'show' : 
                file = open('todos.txt','r')
                todos  = file.readlines()
                file.close()

                # new_todos = [] 
                # for item in todos:
                #     new_item = item.strip('\n')
                #     new_todos.append(new_item)

                new_todos = [item.strip('\n') for item in todos] #list compehension
                
                for index,item in enumerate(new_todos): #nicely prints out the contents of todo
                    #item = item.strip() #simpler than list comprehension maybe
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