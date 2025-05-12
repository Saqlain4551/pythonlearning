   #EXERCISE 1
   #  #empty_list 2 way
empty_list= list() #built_in_function
empty_list= []     #square_bracket

fruits=['banana','apple','orange','mango','papaya'] 
print(fruits)
print(len(fruits))

my_list=['orange','banana','lemon','cherry','strawberrry']
first_my_list= my_list[0]
print(my_list)

middle_index= len(my_list) //2
middle_my_list= my_list[middle_index]
print(middle_my_list)

last_my_list= my_list[-1]
print(last_my_list)

print('first my list:', first_my_list)
print('middle my list:',middle_my_list)
print('last my list:',last_my_list)

#mixed data type list 

my_details= ['Saqlain',{'Age': 19 , 'Country': 'India','State': 'Maharashtra', 'City': 'Mumbra'},True]
print('my details:', my_details)
      

list_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',  'Amazon']
print('list of companies:',list_companies)

print('the number of companies:',len(list_companies))

first_list_companies= list_companies[0]


middle_index= len(list_companies)//2
middle_list_companies= list_companies[middle_index]


last_list_companies= list_companies[-1]


print('first list companies:', first_list_companies)
print('middle list companie:', middle_list_companies)
print('last list comapnies:',last_list_companies)

#modify list companies

list_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',  'Amazon']
list_companies[5]= 'Tata'
print('list of companies:', list_companies)

list_companies.append('Digital Horizon') #added IT companies 
print('list of companies:', list_companies)

list_companies.insert(2,'Apex Technologies') #insert function
print('list of companies:', list_companies)

list_companies[4]= list_companies[4].upper()
print(list_companies)   #uppercase [4] APPLE

list_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',  'Amazon']
string= ['Saqlain','rashid','Sohail','Javed','Junaid','Shlok','Priyansh']

list_companies_and_string= list_companies + string
print(list_companies_and_string)

does_exist= 'Facebook' in list_companies
print(does_exist)  #checking value is exist in a list True 

does_exist= 'Toyota' in list_companies
print(does_exist)    #False

#sort function

list_companies.sort()
print(list_companies)
list_companies.sort(reverse=True)
print(list_companies)

#reverse function

list_companies.reverse()
print(list_companies)

#slice out 1st three companies / last three companies /middle 

first_three_companies= list_companies[:3]
print(first_three_companies)

last_three_companies= list_companies[-3:]
print(last_three_companies)

middle_index=len(list_companies)//2
middle_list_companies=list_companies[middle_index]
print(middle_list_companies)

#remove

list_companies.pop(0)
print(list_companies)

middle_index=len(list_companies)//2
if len(list_companies) % 2 == 0:
          list_companies.pop(middle_index -1)
          list_companies.pop(middle_index -1)
        
else:
        list_companies.pop[middle_index]
print(list_companies)

list_companies.pop(-1)
print(list_companies)

del list_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python'  'SQL')
print(full_stack)

#EXERCISE 2 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)

average_age = sum(ages) / len(ages)
print("Average age:", average_age)

age_range = max_age - min_age
print("Age range:", age_range)

min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Absolute difference (min - average):", min_diff)
print("Absolute difference (max - average):", max_diff)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

if len(countries) % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]
print("First half:", first_half)
print("Second half:", second_half)


first, second, third, *scandic_countries = countries
print("First country:", first)
print("Second country:", second)
print("Third country:", third)
print("Scandic countries:", scandic_countries)






