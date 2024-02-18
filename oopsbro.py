# class Car:
#     def __init__(self,name,model,hp):
#         self.name=name
#         self.model=model
#         self.hp=hp
#     def output(self):
#         print(f"The car is {self.name} and the model is {self.model} it has the power of {self.hp}.")

# my_car = Car("ford", "endieviour", '5000')

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def eat(self):
#         print("animal is eating ")
    
#     def dance(self):
#         print("animal is dancig")

# class Cow(Animal):
#     pass

# ambba = Cow("cow_1")

# ambba.dance()

#method overriding in Python
#Method overriding allows you to redefine a method in a subclass or the derived class previously defined in its parent or the superclass.
# class Animal:
#     def eat(self):
#         print("animal is eating ")

# class Rabbit(Animal):
#     def eat(self):
#         print("i am eating carrot")

# rabbit=Rabbit()
# rabbit.eat()

#super class = function used to give access to the methods of a parent class.
#            returns a temporary object of a parent class when used
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width =width

# class Cube(Rectangle):
#     def __init__(self, length, width,height):
#         super().__init__(length, width)
#         self.height=height

#Walrus operator (:=)
# foods=list()
# while food:= input("what food do you like : ")!="quit":
#      foods.append(food)

# higher order function = A function that accepts a function as an argumnet or returns the function
# def upperr(text):
#     return text.upper()
# def lowerr(text):
#     return text.lower()
# 
# def higher_order(func):
#     text=("Hemendranath chowdary Madhineni")
#     print(func(text))
# higher_order(upperr)
#higher_order(lowerr)

#lambda function = function written in 1 line using lambda keyword
#                   accepts any m=number of arguments, but only has one expression.
#lambda parameters : Expression
# double = lambda x:x*2
# print(double(5))
# add = lambda x,y,z:x+y+z
# print(add(2,3,4))

#sorting
# a=['a','c','b','y','f']
# a.sort(reverse=True)
# print(a)
# 
# students=[("hemendranath",'g',20),
#           ("dhamu","d",45),
#           ("prabhas","b",60),
#           ("obi",'a',100)]
# alpha = lambda alphas:alphas[2]
# 
# students.sort(key=alpha)
# print(students)

#map() = applies a function to each item in an iterable(list,tuple,e.t.c)
# map(function,iterable)
# store = [("shirts",20),("pants",25),("jackets",50)]
# to_price= lambda data:(data[0],data[1]*20)
# store_price=list(map(to_price,store))
# print(store_price)
# for i in store_price:
#     print(i)
#     

#filter() = creates a collection of elements from an iterable for which a function return true
#filter(function,iterable)
# store = [("shirts",20),("pants",25),("jackets",50),("shorts",17)]
# data = lambda cost:cost[1]>=18
# store_map=filter(data,store)
# for i in store_map:
#     print(i)

#list comprehension 
# a=[1,2,3,4,5,6,7]
# 
# 
# list =[x for x in a if x>4]
# print(list)

#dictionary comprehension
# dict1 = {"hema":22,"nandineni": 26,"ramanjaneyulu": 51,"vijaya chandrika": 48}
# 
# for k,v in dict1.items():
#     if v>35:
#         print(k,v)
        
#zip(*iterables) = aggreate element from two or more iterables
# name=["ragner","loki",'ivar']
# age=(46,50,30)
# 
# merge = zip(name,age)
# 
# for i in merge:
#     print(i)
       