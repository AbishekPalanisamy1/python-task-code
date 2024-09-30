# Write a program that counts the number of vowels and consonants in a string
"""
count_vowels=0
count_consonants=0

a=input("Enter your String:")
b=a.casefold()
c=len(b)
print(c)

for i in b:
    if((i=='a'or i=='e'or i=='i'or i=='o' or i=='u')):
        count_vowels+=1
    else:
        count_consonants+=1



print(f" The Number of Vowles is:",count_vowels)
print(f" The Number of Consonants is:",count_consonants)


"""
# Write Program to given string is a palindrome (reads the same forwards and
# backwards).
"""
a=int(input("Enter The number:"))

b=0

t=a
while(a>0):
    r=a%10
    b=b*10+r
    a=a//10

if(b==t):
    print("The number",t,"is an Plaindrome")
else:
    print("The number",t,"is not an Plaindrome")
"""
# Write a program to remove duplicate values in the given string.

a=input("Enter the String")
b=""
for i in a:
    if i not in b:
        b+=i
print(b)
