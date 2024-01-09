# names = ["john smith", "jay santi", "eva kuki"]
# names = [name.title() for name in names]
# print(names)

# usernames = ["john 1990", "alberta1970", "magnola2000"]
# length = [len(user) for user in usernames]
# print(length)

# user_entries = ['10', '19.1', '20']
# list = [float(user) for user in user_entries]
# print(list)

user_entries = ['10', '19.1', '20']
list = sum([float(user) for user in user_entries])
print(list)

