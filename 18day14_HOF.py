# EXERCISE 1 OF HIGHER ORDER FUNCTION 
# 1) DIFFERENT BETWEEN MAP , FILTER , REDUCE ?
'Apply a function to each element of a collection (e.g., list, array) and return a new collection with the results' #MAP
'which returns boolean for each item of the specified iterable  It filters the items that satisfy the FILTEREING criteria' # FILTER
'it does not return another iterable, instead it returns a single value' # REDUCE 

# 2) Explain the difference between higher order function, closure and decorator?

'A function that has access to its own scope and the scope of its outer functions, even when the outer function has returned' # CLOSURE 
'A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure' # DECORATOR 
# HIGHER ORDER FUNCTION 
'''A function can take one or more functions as parameters   
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable'''


# Define a call function before map, filter or reduce, see examples.

def double_number(x):
    return x * 2

def even_number (x):
    return x % 2== 0 

def add_two_num (x, y):
    return x + y

# map 

def double_number(x):
    return x * 2

number = [1, 2, 3, 4, 5, 6]
double_number_list = list(map(double_number, number))
print(double_number_list)  # Output: [2, 4, 6, 8, 10, 12]

# FILTER
def even_number(x):
    return x % 2 == 0

number = [1, 2, 3, 4, 5, 6]
even_number_list = list(filter(even_number, number))
print(even_number_list)  # Output: [2, 4, 6]

# reduce

from functools import reduce

number_str = ['1', '2', '3', '4', '5']

def add_two_nums(x, y):
    return int(x) + int(y)

Total = reduce(add_two_nums, number_str)
print(Total)  

# use for loop and print each country in the countries in a list 

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

print('countries:')
for country in countries:
    print(country)

# print each name 

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

print('\n names:')
for name in names :
    print(name)

# print each number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\n numbers:')
for number in numbers :
    print(number)

# EXERCISE 2 

#Use map to create a new list by changing each country to uppercase in the countries list

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries_uppercase= list(map(str.upper, countries))
print('countries in uppercase :', countries_uppercase)

#  Use map to create a new list with numbers squared

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_squared= list(map(lambda x: x**2, numbers))
print('numbers in squared:', number_squared)

# Use map to change each name to uppercase

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

name_uppercase= list(map(str.upper, names))
print('name in uppercase:', name_uppercase)


# Use filter to filter out countries containing 'land'

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

country_without_land= list(filter(lambda x: 'land' not in x.lower() , countries))
print('country without land :', country_without_land) # output country without land : ['Estonia', 'Sweden', 'Denmark', 'Norway']

# Use filter to filter out countries having exactly six characters

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

country_not_six_char= list(filter(lambda x: len(x) != 6 , countries ))
print('country not six char:', country_not_six_char) # output: country not six char: ['Estonia', 'Finland', 'Denmark', 'Iceland']

# Use filter to filter out countries containing six letters and more

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries_less_than_six = list(filter(lambda x: len(x) < 6, countries))
print("Countries with less than six letters:", countries_less_than_six) # output []

# Use filter to filter out countries starting with an 'E'

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries_not_starting_with_e = list(filter(lambda x: not x.startswith('E'), countries))
print("Countries not starting with 'E':", countries_not_starting_with_e)  # output ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Chain two or more list iterators
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Squared even numbers:", result) # output : Squared even numbers: [4, 16, 36, 64, 100]

# Use reduce to sum all the numbers in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)



# Declare a function called categorize_countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def categorize_countries(lst, pattern):
    return list(filter(lambda x: pattern.lower() in x.lower(), lst))

print("Countries with 'land':", categorize_countries(countries, 'land'))


# Declare a get_first_ten_countries function

def get_first_ten_countries(lst):
    return lst[:10]

# Declare a get_last_ten_countries function
def get_last_ten_countries(lst):
    return lst[-10:]

# Since the countries list has less than 10 items, we'll use a larger list
larger_countries_list = countries * 2
print("First ten countries:", get_first_ten_countries(larger_countries_list))
print("Last ten countries:", get_last_ten_countries(larger_countries_list))











