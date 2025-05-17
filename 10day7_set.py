#  EXERCISE 1 OF sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))   #finding lenght 

it_companies.add('Twitter')   # add a twitter to a it_companies
print(it_companies)

it_companies.update(['microsoft', 'intel', 'SAP']) # to add multiple item of using update function of set 
print(it_companies)

it_companies={'Facebook', 'Apple', 'Microsoft', 'microsoft', 'Oracle', 'Amazon', 'SAP', 'Twitter', 'intel', 'Google', 'IBM'}
it_companies.pop()
print(it_companies)

#diffrence between remove() and Discard()

my_set={1,2,3,4,5,}
my_set.remove(3)
print(my_set)   # in remove  error  come and display in the output 

my_set={1,2,3,4,5,}
my_set.discard(3)
print(my_set)    #in discard error come but not display in the ouput 

my_set.discard(7)

#EXCERCISE 2 OF THE SET 

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B)) # join A and B for using union 
print('A:',A)
print('B:',B)

result=A.intersection_update(B) # A intersection of B 
print('update A with intersection:',A)


print(A.issubset(B))  # subset or not using issubset 
print(A.issuperset(B)) #superset or not using issuperset

print(A.isdisjoint(B))  

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))


#EXERCISE 3 

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age)) #8 length of list is big then set 
age= set(age)
print(age)

print(len(age)) # 5 

# diffrence between string , list,tuple and set

name=("mohd saqlain") # string name 

fruits=['banana','aaple'] # list []

fruits=('banana','apple') # tuple()

age={12,13,53,22,} # set {}

#split the unique word from this sentence

sentence= "I am a teacher and I love to inspire and teach people"

# first remove "" 

sentence=sentence.replace(",","").lower()

word=sentence.split() # split the word

unique_word= set(word)
print('unique word:',unique_word)
print('number of unique word:',len(unique_word))
