import PySimpleGUI as sg

label_f = sg.Text("Enter feet:")
label_i = sg.Text("Enter Inches:")
input_f =sg.Input()
input_i = sg.Input()
convert_button = sg.Button("Convert")

window = sg.Window("Converter",layout = [[label_f, input_f],[label_i, input_i],[convert_button]])


window.read()
window.close()