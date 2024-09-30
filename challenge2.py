# Find the Sum and Average
# Write a Python program that takes a list of numbers as input and calculates and
# prints the sum and average of those numbers

"""
a=[123,32,45,67,89]

b=len(a)

c=0

for i in a:
    c+=i

print("The sum is",c)
print("The Avg is",c//b)
"""


# Reverse a List
# Write a Python function that takes a list and returns a new list with the elements
# reversed. Do this without using the built-in reverse method.
"""
a=[1,2,3,4,5]

b=[]

for i in a[::-1]:
    b.append(i)
print(b)



"""

# Remove Duplicates from a List

"""
a=[11,12,22,11,12,22]

b=[]

for i in a:
    if(i not in b):
        b.append(i)
print(b)

"""

# Find Common Elements

"""
a = [11, 12, 22, 11, 12, 22]
b = []

for i in a:
    if i not in b:  
        for j in a:
            if i == j and a.count(i) > 1:  
                b.append(i)
                break  

print("Duplicate values:", b)

"""

# Count the Occurrences of an Element

"""

a = [11, 12, 22, 11, 12, 22]
b = int(input("Enter the number: "))


index = 0 

for i in range(len(a)):
    if a[i] == b:
        index = i 
        print(f"The index of {b} is: {index}")
        
if(index==0):
    print(f"{b} is not found in the list.")
"""


