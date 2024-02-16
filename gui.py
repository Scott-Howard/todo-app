from modules import functions as fn
import PySimpleGUI as sg

label = sg.Text("Type in a todo.")
input = sg.InputText(tooltip="Enter a todo", key = "todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values = fn.get_todos(), key = 'todos', enable_events = True,
                      size = [45,10])

window = sg.Window('Todo App', 
                   layout=[[label],[input,add_button],[list_box, edit_button]],
                   font = ("Helvetica", 16)) # layout needs to be a list of lists for layout widgets, each row is a list and need to be widget types.

while True:
    event,values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window['todos'].update(values = todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = fn.get_todos()
            index =todos.index(todo_to_edit)
            todos[index] = new_todo
            fn.write_todos(todos)
            window['todos'].update(values = todos)
        case 'todos':
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
