# Write a program to check Armstrong number
"""


a=1634
b=0

t=a

while(a>0):
    r=a%10
    b=b+(r*r*r)
    a=a//10
print(b)
if(t==b):
    print("armstrong")

else:
    print("Not an armstrong")

"""


# Write a program to check palindrome number.

"""
a=127
b=0

t=a

while(a>0):
    r=a%10
    b=b*10+r
    a=a//10

if(t==b):
    print("Palindrome")

else:
    print("Not Palindrome ")

"""
# Write a program to print sum of digits.
"""
a=456

c=str(a)
b=0
for i in c:
    b+=int(i)
print(b)
"""
# Print the Fibonacci series for first 12 numbers
"""
a=0
b=1
c=12


for i in range(c-1):
    d=a+b
    a=b
    b=d
print(d)


"""

# Write a Program to print the multiplication table.
"""


a=5
b=10

for i in range(1,b+1):
    print(i ,"*",a,"=",i*a)

"""

#    How to find the factorial of number 5.
"""


a=5
f=1
for i in range(1,a+1):
    f=f*i
print(f)

"""

# Write a Program to Check Whether a Number is Prime or Not


# a=7

# count=0

# for i in range(2,int(a**0.5)+1):
#     if(a%i==0):
#         count+=1

# if(count==0):
#     print("prime")
# else:
#     print("not prime")


# pattern
# # Function to print full pyramid pattern
# n=5
# for i in range(1, n + 1):
      
#     for j in range(n - i):
#         print(" ", end="")
        
      
#     for k in range(1, 2*i):
#         print("*", end="")
#     print()
   

# Function to demonstrate printing pattern of numbers



# n=5
# num=0

# for i in range(0,n):
#     num=0+1

#     for j in range(0,i):

#         print(num, end=" ")
#         num=num+1
#     print("  ")



# n=5
# num=0

# for i in range(0,n):
    

#     for j in range(0,i):

#         print("*", end=" ")
       
#     print("  ")

# for i in range(n,0,-1):

#     for j in range(0,i):

#         print("*",end=" ")

#     print("")


# n = 6


# for i in range(n, 0, -1):  
#     for j in range(i, n + 1):
        
#         print(j, end=" ") 
        
#     print()  
