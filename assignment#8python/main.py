#BTypes of modules
#1.built in modules
# import math
# print(math.sqrt(25))

# #user defined modules (custom module)
# def add(a, b):
#     sum=(a + b)
#     print(sum)
#     return sum
# add(3,5)

# #third party modules 
# import requests
# response = requests.get("https://www.example.com")
# print(response.status_code)

# #global function
# a="Hello world!"
# def func():
#     print(a)
# func()    

# #types of python function
# #1.built in function
# a=(1,2,3,4.5)
# print(len(a))
# print(type(a))

#2. Pass by value vs pass by reference
# def modify_value(x):
#     x = 10
#     print("Within function:", x)
# modify_value(15)    

# #Immutable object (integer)
# x = 5
# print("Original:", x)
# modify_value(30)
# print("After function:", x)

#pass by reference
# def modify_list(lst):
#     print("Inside function - before modification:", lst)
#     lst.append(5)
#     print("Inside function - after modification:", lst)

# my_list = [1, 2, 3]
# modify_list(my_list)

#key word arguement
# def bio_data(name,age):
#     print("Name:",(name),"Age:",(age))
#     return
# bio_data(age=32,name="Ali")    
   
#unpacking itterable

# def list_1(a,b,c,d):
#     print(a,b,c,d)
# list_2=(1,2,3,4)
# list_1(*list_2)
# print(type(list_1))

# x=[1,5]
# print(range(*x))
# print(list(range(*x)))
# print(type(x))

#key-word arguments and position arguements as args & kwargs

# def func(name,age=48):  #key word argument
#     print("My name is:",name ,"and my age is",age ,"years old")
# func("Shazia",48)

# def hello(*args,**
#           kwargs):
#     print(args)
#     print(kwargs)
# hello("Zia","Ali",32,46)

#recursive function :a function that repeats
# def value(n):
#     if (n==0):     #basecase
#      return 
#     print(n)
#     value(n-1)      #repeat function

# value(5) 

# generator function

def simple_generator(x,y):

    yield x+y
    yield x-y
    yield x*y

# Create a generator object
obj = simple_generator(10,2)

print(next(obj))
print(next(obj))
print(next(obj))



