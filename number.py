# x=100

# def ak():
#     global x
#     x=50
#     print(x)
# ak()
# def fun():
#     yield 8
# a=fun()
# print(a.__next__())

# mylist=[1,2,3,4,5,6]
# mylist=iter(mylist)

# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))


# Itertator

# alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# alpha=iter(alpha)
# while True:
#     print(next(alpha), end=" ")


# Create a simple calculator operations using function.
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
# def calculator():
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     choice = input("Enter choice (1/2/3/4): ")
#     num1 =int (input("Enter first number: "))
#     num2 =int(input("Enter second number: "))
#     if choice == '1':
#         print(f"Result: {num1} + {num2} = {add(num1, num2)}")
#     elif choice == '2':
#         print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
#     elif choice == '3':
#         print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
#     elif choice == '4':
#         print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
#     else:
#         print("Invalid input")
# calculator()



# Create a Python function that takes a string as input and counts the number of
# vowels and consonants in the string


# def words(string):
#     a=string.lower()
#     count=0
#     count1=0
#     for i in a:
#         if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
#             count+=1
#             print(f"vowels are {i}")
            
#         else:
#             count1+=1
#             print(f"consonats are {i}")
            
#     print(f"The total numvber of vowles{count}")
#     print(f"The total numvber of conosants{count1}")
# words(input("Enter the string"))



# from functools import reduce

# def sum(a,b):
#     return a+b
# result=reduce(sum,[1,2,3,4])
# print(result)

# Write a Python program to square and cube every number in a given list of integers
# using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def square_and_cube(numbers):

#     squared = list(map(lambda x: x ** 2, numbers))
#     cubed = list(map(lambda x: x ** 3, numbers))
#     return squared, cubed

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squared_numbers, cubed_numbers = square_and_cube(num)

# print("Squared numbers:", squared_numbers)
# print("Cubed numbers:", cubed_numbers)

# Write a Python program to find numbers divisible by nineteen or thirteen from a list
# of numbers using Lambda.

# def divisible(numbers):
    
#     divide = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
#     return divide


# numbers = [13,19,26,45,67,876,455,28]


# result = divisible(numbers)

# print("Numbers divisible by 19 or 13:", result)

# Write a Python program to calculate the sum of the positive and negative numbers
# of a given list of numbers using the lambda function.


# def numbers(num):

#     positive=list(filter(lambda x:x>=0,num))

#     negative=list(filter(lambda x:x<0,num))

#     return positive,negative

# num=[2,10,-12,-100,100,-5456,343,0]

# positive,negative=numbers(num)

# print(f"Positive number {positive}")
# print(f"Negative numbers {negative}")


# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]



# def fun(subject):
#     sort=sorted(subject,key=lambda x:x[1])
#     return sort

# subject= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# result=fun(subject)
# print(result)