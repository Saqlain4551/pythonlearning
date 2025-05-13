#EXERCISE 1  CREATE A EMPTY TUPLE 
emp_tuple= tuple()
my_tuple=()  

brother=('hasnain','usman','mujahid','ashraf','shahid')
sister=('akela','aliya','shifa','roshni','aina')
siblings= brother + sister
print('siblings:', siblings)
print(len(siblings))

siblings= ('hasnain', 'usman', 'mujahid', 'ashraf', 'shahid', 'akela', 'aliya', 'shifa', 'roshni', 'aina')

siblings= list(siblings)

father= ['javed Ali']
mother= ['Noor Afza']

family_members= siblings + father + mother
print('family members :', family_members)

siblings= tuple(siblings)

#EXERCISE 2 UNPACKING SLICING 

family_members = ('hasnain', 'usman', 'mujahid', 'ashraf', 'shahid', 'akela', 'aliya', 'shifa', 'roshni', 'aina', 'javed Ali', 'Noor Afza')

*siblings, father , mother = family_members

parents= (father , mother)
siblings = tuple(siblings)

print('parents:', parents)
print('siblings:',siblings)

#CREATE FRUIT VEGETABLE ANIMALS PRODUCT AND JOIN 

fruits= ('banana','watermelon','grapes', 'orange', 'mango')
vegetable=('tomoto','potato','carrot','beets','flower')
animal_product= ('meet', 'dairy','eggs','honey','cheese')

food_stuff_tp = fruits + vegetable + animal_product
print('food stuff tp:', food_stuff_tp )

food_stuff_tp =  ('banana', 'watermelon', 'grapes', 'orange', 'mango', 'tomoto', 'potato', 'carrot', 'beets', 'flower', 'meet', 'dairy', 'eggs', 'honey', 'cheese')
food_stuff_tp= list(food_stuff_tp)

middle_index= len(food_stuff_tp ) //2
middle_food_stuff_tp = food_stuff_tp[middle_index]
middle_food_stuff_tp= food_stuff_tp[7]
print(middle_food_stuff_tp)


first_three_item = food_stuff_tp[0:3]
print('first three items :', first_three_item)

last_three_item= food_stuff_tp[-3:]
print('last three itmes:', last_three_item)

food_stuff_tp =  ('banana', 'watermelon', 'grapes', 'orange', 'mango', 'tomoto', 'potato', 'carrot', 'beets', 'flower', 'meet', 'dairy', 'eggs', 'honey', 'cheese')
del food_stuff_tp # delete the food_stuff_tp tuple

#checking function 

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)

print('Iceland' in nordic_countries)










