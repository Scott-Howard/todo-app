password = input("enter a new password: ")
result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for char in password:
   if char.isdigit():
       digit = True

result["digits"] = digit

upcase = False
for char in password:
   if char.isupper():
       upcase = True
result["uppercase"] = upcase
#print(result)

if all(result.values()):
    print("Strong Password")
else:
    print('Weak Password')