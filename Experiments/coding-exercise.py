'''
steps 
enter a whole number - lower bound
enter a whole number - upper bound
generate a random integer between the upper and lower bound
'''
import random

seed = random.seed(1)

lower = int(input('Enter an integer for the lower bound: '))
upper = int(input('Enter an integer for the upper bound: '))

output = random.randint(lower, upper)
print(output)

