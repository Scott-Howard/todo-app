import PySimpleGUI as sg

# def convert(feet, cm):
#     try:
#         if feet > 0:
#             out = float(feet)*2.54
#         elif cm > 0:
#             out = float(cm)/2.54
#         return out
#     except:
#         print("not a number")
    

sg.theme("Black")


label_f = sg.Text("Enter feet:")
label_i = sg.Text("Enter Inches:")
input_f =sg.Input()
input_i = sg.Input()
convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

window = sg.Window("Converter",layout = [[label_f, input_f],[label_i, input_i],[convert_button, exit_button]])


while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")



window.close()