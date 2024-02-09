prompt = input("Add a new member: ") 
 
file = open('members.txt', 'r')
mem_list = file.readlines()
file.close
print(mem_list)

mem_list.append(prompt +"\n")
print(mem_list)
file  = open('members.txt', 'w')
file.writelines(mem_list)
file.close()

