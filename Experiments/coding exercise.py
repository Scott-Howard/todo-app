# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     output = (value/total_value)*100
#     print(f"That is {output}%")
# except ValueError:
#     print("You need to enter a number. Run the program again")
# except ZeroDivisionError:
#     print('Your total cannot be zero')

# colors = [11, 34, 98, 43, 45, 54, 54]

# for color in colors:
#     if color > 50:
#         print(color)

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_g = max(grades)
#     min_g = min(grades)
#     return (f"Max:{max_g}, Min:{min_g}")

# print(get_max())

# get_max()

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_g = max(grades)
#     min_g = min(grades)
#     return max_g,min_g

# [a,b] = get_max()
# print(f"Max:{a}, Min:{b}")

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#     return maximum
    
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
 
# print(fahrenheit)

def avg_list(bag):
    den = len(bag)
    num = 0
    for thing in bag:
        num = int(num) + int(thing)
    return(num/den)