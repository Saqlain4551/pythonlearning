#EXERCISE OF FUNCTION 
def add_two(num1 , num2):   # add two number two parameter
    total= num1 + num2 
    return (total)
print(add_two(2 , 9))  # 11

def area_of_circle(r):
    PI= 3.14
    area= PI * r ** 2
    return area
print('area of a circle:',area_of_circle(20))  # 10 = 314 AND  20 = 1256

def add_all_nums(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        return "Error: All arguments must be numbers (int or float)."
    
    return sum(args)
print(add_all_nums(1, 2, 3.5)) 
print(add_all_nums(1, "two", 3))  


# conert C to F 
def convert_celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        return "Error: Input must be a number (int or float)."
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(0))      
print(convert_celsius_to_fahrenheit(100))    
print(convert_celsius_to_fahrenheit("cold")) 


def check_season(Month):
    seasons = {
        "Winter": ["December", "January", "February"],
        "Spring": ["March", "April", "May"],
        "Summer": ["June", "July", "August"],
        "Autumn": ["September", "October", "November"]
    }
    return seasons
print(check_season("March"))    
print(check_season("october"))   
print(check_season(" JULY "))    
print(check_season("Hello"))  

# def slope 
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined"
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 4))  

# quadratic equation

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solution"
    x1 = (-b + (discriminant)**0.5) / (2*a)
    x2 = (-b - (discriminant)**0.5) / (2*a)
    return x1, x2

print(solve_quadratic_eqn(1, -3, 2)) 

# print list 
def print_list(lst):
    for item in lst:
        print(item)

print_list(['apple', 'banana', 'cherry'])

#reversed list
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


print(reverse_list([1, 2, 3, 4, 5]))        


def reverse_list1(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


print(reverse_list1(['A' , 'B' ,'C' ]))       

# CAPITILIZED LIST 

def capitalize_list_items(lst):
    capitalized = []
    for item in lst:
        capitalized.append(item.capitalize())
    return capitalized

print(capitalize_list_items(['apple', 'banana']))  

# ADD ITEM 

def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # 2 7 9

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers(5))   

# ODD 

def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))   

# EVEN 

def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(25))  


# EXERCISE 2 

def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("The number of odds are", odds)
    print("The number of evens are", evens)

evens_and_odds(100)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))  


def is_empty(value):
    if value:
        return False
    return True

print(is_empty(""))        
print(is_empty([1, 2]))    

# EXERCISE 3 

def are_items_unique(lst):
    return len(lst) == len(set(lst))

print(are_items_unique([1, 2, 3]))     # True
print(are_items_unique([1, 2, 2]))     # False


def same_data_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True

print(same_data_type([1, 2, 3]))       # True
print(same_data_type([1, "2", 3]))     # False


# countries 
countries_data = [
    {'name': 'China', 'population': 1439323776, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1380004385, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 331002651, 'languages': ['English']},
    
]
print (countries_data)








