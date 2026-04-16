'''
OOP'S(object oriented programming langauge)
Classes
Objects
Attributes
Methods

OOP'S
-------
#object-oriented programming langauge is a style of programming where we model real-world things as objects that contain both
data and functions()
#reusable of code
#and also scalability 

Class-->(template,blueprint)class is a blue-print or template that defines what kind of data and behaviour of a certain type of
object will have
syntax:-
        class Class_name:
            pass
example:-
class car:
    pass

Object-->Instance of class or An object as a real instance created from a class.it is the actual thing that exists memory while
the program running

example:-
class car:
    pass
car1=car() #these are object
car2=car() #these are object

Attributes-->these are variables that store data related to a class or object'''

class car:                          #here car is the class
    def __init__(self,brand,color): 
        self.brand = brand
        self.color = color
car_1 = car("Toyota","black")
car_2 = car("Thar","white")
print(car_2.brand,car_2.color)

class cat:
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
cat_1 = cat("persian","white")
cat_2 = cat("stray","brown")
print(cat_1.breed,cat_1.color)


class dog:
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
dog_1 = dog("pomerian","orange")
dog_2 = dog("husky","white")
print(dog_1.breed,dog_1.color)



class lays:
    def __init__(self,flavour,color):
        self.flavour = flavour
        self.color = color
lays_1 = lays("blue masala","blue")
lays_2 = lays("onion cream","green")
print(lays_1.flavour,lays_1.color)


class chocolates:
    def __init__(self,name,flavour):
        self.name = name
        self.flavour = flavour
chocolates_1 = chocolates("dairymilk","caramel")
chocolates_2 = chocolates("milkybar","strawberry")
print(chocolates_1.name,chocolates_1.flavour)


class fruits:
    def __init__(self,name,taste):
        self.name = name
        self.taste = taste
fruits_1 = fruits("apple","sweet")
fruits_2 = fruits("mango","sour")
print(fruits_2.name,fruits_2.taste)


class companies:
    def __init__(self,name,domain):
        self.name = name
        self.domain = domain
companies_1 = companies("amazon","marketplace")
companies_2 = companies("sutherland","MNC")
print(companies_1.name,companies_1.domain)





































