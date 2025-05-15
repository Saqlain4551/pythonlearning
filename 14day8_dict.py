 # EXERCISE 1 OF DICTIONARY
dog={}
dog['name']= "Mauku"
dog['age']= 7
dog['breed']='poodle'
dog['leg']=4
dog['color']='White'
print ('dog:',dog)  #dog: {'name': 'Mauku', 'age': 7, 'breed': 'poodle', 'leg': 4, 'color': 'White'}

#create a student dictionary
Student={'first_name': 'Mohd Saqlain', 'last_name': 'Maniyar','age': 19,'gender': 'Male','city': 'Mumbra','marital_status': 'Single','skill': ['python','mysql','cricket','photography'],'country':'India','address': 'shilphata','pincode':400612}
print(len(Student))
print('Student:', Student)

print('value of a skill:',Student['skill'])  #get a skill value 
print('data type of skill:',type(Student['skill']))  # data type skill in a list

#modify skill value
Student={'first_name': 'Mohd Saqlain', 'last_name': 'Maniyar','age': 19,'gender': 'Male','city': 'Mumbra','marital_status': 'Single','skill': ['python','mysql','cricket','photography'],'country':'India','address': 'shilphata','pincode':400612}
Student['skill']= ['editor','communication','cricket','python','photography']
print(Student)

key_list=list(Student.keys())
print(key_list)     #get key of student

value_list=list(Student.values())    # get value of Student
print(value_list)

print(Student.items())

del Student['marital_status']
print(Student) # delete one dictionary item using del 

del Student # delete a dict
print(Student)