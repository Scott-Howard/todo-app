from modules import functions as fn
import PySimpleGUI as sg

label = sg.Text("Type in a todo.")
input = sg.InputText(tooltip="Enter a todo", key = "todo")
add_button = sg.Button("Add")

window = sg.Window('Todo App', 
                   layout=[[label],[input,add_button]],
                   font = ("Helvetica", 16)) # layout needs to be a list of lists for layout widgets, each row is a list and need to be widget types.

while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)

window.close()
