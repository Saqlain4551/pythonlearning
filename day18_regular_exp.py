import re

text= 'I love to teach python and javaScript'

pattern= '[a-z]'  
 # if we use this pattern [A-z] then output is - ['I', 'l', 'o', 'v', 'e', 't', 'o', 't', 'e', 'a', 'c', 'h', 'p', 'y', 't', 'h', 'o', 'n', 'a', 'n', 'd', 'j', 'a', 'v', 'a', 'S', 'c', 'r', 'i', 'p', 't']

matches= re.findall(pattern , text)
print(matches)  # output - ['l', 'o', 'v', 'e', 't', 'o', 't', 'e', 'a', 'c', 'h', 'p', 'y', 't', 'h', 'o', 'n', 'a', 'n', 'd', 'j', 'a', 'v', 'a', 'c', 'r', 'i', 'p', 't']


