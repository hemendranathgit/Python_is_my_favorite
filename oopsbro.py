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

#