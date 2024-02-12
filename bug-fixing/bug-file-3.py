# def speed(distance, time):
#     return distance / time
    
# print(speed(200, 4))


# def speed(distance, time):
#     return distance / time
    
# print(speed(300, 5))

# def parse(user_input):
#     """Extract the values split by a comma in a string
#     and return the two values via a dictionary.
#     """
#     # Get the two values in a list
#     parts = user_input.split(",")
    
#     # Store the two values in variables 
#     lower_bound = float(parts[0])
#     upper_bound = float(parts[1])
    
#     # Inject the values in a dictionary
#     return {"lower_bound": lower_bound, "upper_bound": upper_bound}

# # from parsers import parse 
# import random
 
# # Ask the user to enter a lower and an upper bound divided by a comma
# user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")
 
# # Parse the user string by calling the parse function
# parsed = parse(user_input)
 
# # Pick a random int between the two numbers
# rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
 
# print(rand)

import PySimpleGUI as sg
 
label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
 
window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1], 
                            [option2], 
                            [option3], 
                            [option4],
                           ])
 
window.read()
window.close()