# EXERCISE 1 OF LIST COMPREHENSION 

# filter only negative number and zero 

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_even_number = [i for i in numbers if i % 2 == 0 and i <= 0]
print(negative_even_number)  # [-4, -2, 0]

# FLATTEN LIST OF LIST 

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

number = [(i , i**0, i**1, i**2, i**3, i**4, i**5,) for i in range(0, 11)]
print(number)  # pattern 

# flatten list to new list 

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [[country.upper(), country[:3].upper(), capital.upper() ] for [[country , capital]] in countries] 
print(result)  # [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# change into dictionary

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

result = [{'first_name': first.upper(), 'last_name': last.upper()} 
          for [[first, last]] in names]

print(result)


# change list of lists  into concatenated strings

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [f"{first} {last}" for [[first, last]] in names]
print(full_names)

# lambda for slope 

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) # slope 

y_intercept = lambda x, y, m: y - m * x # formula 

m = slope(2, 4, 6, 12)        # slope between (2,4) and (6,12)  # 2.0
b = y_intercept(2, 4, m)      # y-intercept using point (2,4)   # 0.0

print("Slope:", m)
print("Y-Intercept:", b)



