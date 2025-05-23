

import random

# String
name = "John Doe"
print("Name:", name)

# List
fruits = ["Apple", "Banana", "Cherry"]
print("Fruits:", fruits)

# Tuple
colors = ("Red", "Green", "Blue")
print("Colors:", colors)

# Dictionary
person = {"name": "Jane Doe", "age": 30}
print("Person:", person)

# Function
def greet(name):
    print("Hello,", name)

greet("Saqlain")

# Loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("Number:", num)

# Using random module
random_number = random.randint(1, 10)
print("Random Number:", random_number)

# Accessing dictionary items
for key, value in person.items():
    print(key, ":", value)

# Accessing list items
for fruit in fruits:
    print("Fruit:", fruit)

# Accessing tuple items
for color in colors:
    print("Color:", color)

#printing prime number 
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# multiplication table 
num = 12

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

