# math function
# import math
# pi =3.14
#print(round(pi))
#print(math.floor(pi))
#print(math.ceil(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))

#string slicing
#[start:stop:step]
#a="hemendranath"
# print(a[::2])
# print(a[0:4])
#print(a[::-1])
# website="http://google.com"
# website1="http://youtube.com"
# slice=slice(7,-4)
# print(website[slice])
# print(website1[slice])

#logical Operators
#while looop
# is a statement that execute the block of code untill the condition remains true

#for loop 
#a for loop is used for iterating over a sequece.

#set
#set is sa collection of unordered,unindexedand no duplicate values
# new_set = {1,2,3,4,5}
# set_2={4,5,8,9}
# new_set.update(set_2)
# set_2.add(10)
# print(new_set.intersection(set_2 ))
# print(new_set)

#dictionary
# dictionary is a changeable,unorderd collection of key:value pairs Fast 
# because they using hashing, allow us to accessa value 
# dict1={'india':'new delhi',
#        "usa" : "washington DC",
#        "sweden" : "stockhlam"
#        }
# print(dict1["india"])
# print(dict1.keys())
# print(dict1.values())
# dict1.pop("india")
# for key,value in dict1.items():
#     print(key,value)

#function = is a block of code which is executed only when it is called

#scope
#Local scope = a variable only available inside the region it is created
#Global scope = is a variable which is used inside and outside the function or loops.

# *args = parameter that will pack all arguments into a tuple
#         useful so that a sunction can accept a varying amount of arguments
# def hema(*staff):
#     sum1=0
#     for i in staff:
#         sum1+=i
#     return sum1

# print(hema(1,2,3,4))

#**kwargs key word arguments = parameter that will pack all arguments into a dictionary
#  useful so that a function can accept varying amount of keyword arguments

# def hello(**kwargs):
#     print("hello",end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")
# hello(title="Mr.",first="hemendranath",Middle="Chowdary",Last="Madhineni")

# string format = str.format() = optional method that gives users more control when
#                                displaying the output.
# name="hemendranath"
# age = 23
# 
# print("hello Mr.{} he is {} old".format(name,age) )
# number = 3.14159
# value=23432233
# print(f"the number pi is {number:.2f}")
# #binary
# print("the binary number is {:b}".format(value))
# print("the octal number is {:o}".format(value))#octal
# print("the hexa number is {:x}".format(value))#hexa
# print("the number is {:,}".format(value))

# import random
# x=random.randint(1,6)
# 
# mylist=['rock','papers','scissors']
# random.choice(mylist)
# random.shuffle(mylist)
# print(mylist)

#file handling
# f=open("hi.py",'r')
# print(f.mode)
# with open("hi.py",'r') as f:
#     print(f.readline())
# import os
# path = "C:\\Users\\hemendranath\\OneDrive\\Desktop\\python\\assignment2.txt"

# if os.path.exists(path):
#     print("Exist")
# else:
#     print("No")

