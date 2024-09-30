# Write a Python program to check that a string contains only a certain set of
# characters (in this case a-z, A-Z and 0-9).

# import re

# a='Hello ABishek @#$% 2345'

# b=re.findall('[a-zA-z0-9]',a)

# print(b)



import re
my_string = input('enter a string ')
p = re.compile('ab?')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')