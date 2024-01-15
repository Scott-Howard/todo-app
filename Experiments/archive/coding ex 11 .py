# password = input("enter a new password: ")
# result = {}

# if len(password) > 7:
#     result["Length"] = True
# else:
#     result["Length"] = False

# if all(result.values()):
#     print("Strong Password")
# else:
#     print('Weak Password')

# password = input("enter a new password: ")

# if len(password) > 7:
#     print('Great password there')
# elif len(password) == 7:
#     print('Password is OK, but not too strong')
# else:
#     print('Your password is weak')

# day_temp = {'Morning':(23.0,23.0,23.0),"noon":(35.1,23.0,23.0),"evening":(23.9,23.0,23.0)}

length = float(input("Enter length: "))
width = float(input("Enter width: "))
 
perimeter = (length + width) * 2
area = length * width
 
print("Perimeter is", perimeter)
print("Area is", area)
 
if perimeter < 14 and area > 10:
    print("OK")
else:
    print("NOT OK")