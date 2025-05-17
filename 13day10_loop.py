#EXERCISE 1 OF LOOPS 
for i in range(11):
    print(i)     # 0 to 10 using for loop

i = 0
while i <= 10:
    print(i) # using while print 0 to 10
    i += 1


for i in range (10 ,-1,-1):
    print(i)             # print 10 to 0 with using for 

i=10
while i >= 0:
    print(i)  # same but using while
    i -= 1

for i in range(1,8):
    print('#' *i)   # print 7 # 

for i in range (8):
    for j in range (8):
        print('#', end= "")   # print 8 *8 ##########
    print()                                ######### like this 

for i in range (11):
    print(f"{i} x {i} = {i*i}")   # print table 0x0=0 till 10 x 10 = 100

sub_list=[ 'python', 'java','sql','html']
for sub in sub_list:
    print(sub)     # print the list 

for i in range (0 ,11 ,2):
    print(i)

for i in range(0, 101):
    if i % 2 == 0:   # print 0 to 100 only even
        print(i)

for i in range (0, 101):
    if i % 2 != 0:
        print(i)   # print 0 100 only odd

total=0

for i in range (101):                     # print sum of all number using loop
    total += i # add the current number 
    print("the sum of number is :", total)

even_sum= 0
odd_sum=0

for i in range (101):              # print even or odd sum number using loop
    if i % 2  == 0:
         even_sum += i
    else:
        odd_sum += i

print("The sum of all evens is", even_sum)
print("The sum of all odds is", odd_sum)