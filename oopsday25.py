'''
#Polymorphsim-->this allows object of different classes to be treated as instance of the same base class,
with methods behaving differently based on the actual object type.
example:-
print(len("python"))
print(len([1,2,3]))

Method overloading-->this defines multiple methods with the same name but different parameters
such as (number, type, or order)in the same class.



class calculator:
    def add(self, a, b=5, c=6):
        return a+b+c
cal = calculator()
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))

class calculator:
    def sub(self, a, b=3, c=1):
        return a-b-c
cal = calculator()
print(cal.sub(9))
print(cal.sub(9,8))
print(cal.sub(7,6,5))

Method overriding-->this occurs in the child class, redefining a parent class method with the same signature for runtime.

class animal:
    def speak(self):
        return"Sound"
class dog(animal):
    def speak(self):
        return"bow"
DOG = dog()
print(DOG.speak())


class animal:
    def speak(self):
        return"Sound"
class cat(animal):
    def speak(self):
        return"Meow"
CAT = cat()
print(CAT.speak())


class parent:
    def speak(self):
        return"sound"

class mother(parent):
    def speak(self):
        return"chetha rascel"

MOTHER = mother()
print(MOTHER.speak())

Operator Overloading-->this customizes operator like +, - for user-defined classes by implementing specific methods.
example:- __add__, __sub__

#__add__
class someone:
    def __init__(self, a, b):  #this constructor is constant
        self.a = a
        self.b = b

    def __add__(self, other):  #add fucntionality
        return someone(self.a + other.a, self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"
any = someone(2,3)
so = someone(5,9)
print(any + so)

#__sub__
class someone:
    def __init__(self, a, b, c):  
        self.a = a
        self.b = b
        self.c = c

    def __sub__(self,other):
        return someone(self.a - other.a, self.b - other.b, self.c - other.c)
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
any = someone(2,3,9)
so = someone(5,9,6)
print(any - so)

Data abstraction-->this hidess complex implementation details, exposing only essential features via abstarct class or interface.


from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
circle = circle(5)
print(circle.area())
































