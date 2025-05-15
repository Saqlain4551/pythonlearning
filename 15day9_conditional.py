# # EXERCISE 1 OF CONDITIONAL 
# n=int(input("Enter your age "))
# if n >= 18:                     # IF age is 18 or 18 above then only he can drive 
#     print("You are old enough to drive ")
# else:
#     print("Sorry! You are  now not applicable to drive  ") 

# my_age= 19
# your_age= int(input("Enter your age: "))

# age_diff=abs(my_age - your_age)
# print(age_diff)

# #compare the my age and your age
# if my_age < your_age :
#      if age_diff== 1 :
#          print("you are 1 year older than me ")
#      elif age_diff==5:
#         print("you are 5 year older than me")
#      elif age_diff==2 :
#         print("you are 2 year older than me ")
#      else:
#          print("You are older than me  ")
# elif my_age > your_age:
#     print("I am older than you")
# else:
#     ("we are same age ")

# #check the the number who is greater or smaller or equal 
# a= int(input("Enter a first number:"))
# b= int(input("Enter a second number:"))
# if b > a :                                              
#     print("b is greater ")
# elif b < a :
#     print("a is greater")
# else:
#     print("equal number ")

# # EXERCISE 2 

# n= int(input("Enter a Marks"))
# if n >= 90:
#     print("Outstanding!!")
# elif n >= 80:
#     print("A Grade")
# elif n >= 70:
#     print("B Grade")
# elif n >= 60:  
#     print("C Grade")
# elif n >= 50:  
#     print("D Grade")
# elif n >= 40:  
#     print("E Grade")
# else:
#     print("Fail!!")

# # check the Season

# n = input("Enter the month: ").strip().capitalize()

# autumn_months = ("September", "October", "November")
# winter_months = ("December", "January", "February")
# spring_months = ("March", "April", "May")

# if n in autumn_months:
#     print("The season is Autumn")
# elif n in winter_months:
#     print("The season is Winter")
# elif n in spring_months:
#     print("The season is Spring")
# else:
#     print("The season is Summer")

# fruits = ['banana', 'orange', 'mango', 'lemon']

# def add_fruit(fruit):
#     if fruit.lower() in fruits:
#         print('That fruit already exists in the list')
#     else:
#         fruits.append(fruit.lower())
#         print('Fruit added successfully. Modified list:', fruits)

# fruit_to_add = input("Enter a fruit: ")
# add_fruit(fruit_to_add)

# Exercise 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person)

if 'skills' in person :
    skills= person['skills']
    middle_index= len(skills)//2
    print("Middle skills:", skills[middle_index])

print("Middle skills:", skills[middle_index])

#if skill is exists in person and skill is java and react then print he is front end developer

if 'skills' in person:
    skills = set(skill.lower() for skill in person['skills'])
    if skills == {'javascript', 'react'}:
        print("He is a front end developer")
    elif skills.issuperset({'node', 'python', 'mongodb'}):
        print("He is a backend developer")
    elif skills.issuperset({'react', 'node', 'mongodb'}):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# if person married and he belong to finland then print his detail

if person['is_marred'] and person['country'].lower()== 'finland':
    print({person['first_name']}, {person['last_name']}, {person['is_marred']},{person['country']})


