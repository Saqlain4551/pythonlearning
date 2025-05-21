# EXERCISE 1 OF MODULE 
import random
import string

def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

print(random_user_id())


# modify and user id gen by user from random user id and take input 2 first for char and second for id 

def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs: "))
    characters = string.ascii_letters + string.digits
    return  [''.join(random.choice(characters) for _ in range(num_chars)) for _ in range(num_ids)]

print(user_id_gen_by_user())


def rgb_color_gen():
    return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

print(rgb_color_gen())

# # EXERCISE 2 

def list_of_hexa_colors(n):
    return [f"#{random.randint(0, 0xFFFFF):06x}" for _ in range(n)]

print(list_of_hexa_colors(5)) # output will come this way #0cc89e like that 

def list_of_rgb_colors(n):
    return [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range (n)]

print(list_of_rgb_colors(3))


def generate_colors(color_type, n):
    if color_type == 'hexa':
        return [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(n)]
    elif color_type == 'rgb':
        return [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range(n)]
    else:
        return "Invalid color type"

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))


# EXERCISE 3

def shuffle_list(lst):
    return random.sample (lst,len(lst))  # select the random element from the list 

print(shuffle_list([1, 2, 3, 4, 5]))



def unique_random_numbers(): # gen random number 
    return random.sample(range(10), 7)   # he select betwen 1 to 10 only 7 unique random number 

print(unique_random_numbers())  # [3,8,4,5,2,0,9]












  