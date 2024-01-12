user_prompt ="Enter a todo:"

todos = [] # initialise an emppty list
while True :
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)