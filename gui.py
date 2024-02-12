from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo.")
input = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window('Todo App', layout=[[label],[input,add_button]]) #needs to be a list of lists for layout widgets, each row is a list and need to be widget types.
window.read()
window.close()
