'''
#Encapsulation-->the principle of bunding data(Attribute) and methods that operates on that data into a single unit, which is a class

class BankAC:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
Acc = BankAC(15000)
Acc.deposite(7000)
print(Acc.get_balance())

Inheritance-->this allows a child class(subclass) to acquire attributes and methods of a parent class(base class) this is called inheritance.
Super()-->calls methods from the parent class
1.Single Inheritance:-acccessing only single method of the class from base class is called single inheritance
example:-
class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is called method")
obj = child()
obj.display()

2.Multiple Inheritance:-a child class inherits form more than one parent class

example:-
class Father:
    def skill_1(self):
        print("Father: hard working")
class Mother:
    def skill_2(self):
        print("Mother:cooking")
class child(Father,Mother):
    def all_skills(self):
        print("Child:coding")
any = child()
any.skill_1()
any.skill_2()
any.all_skills()'''




































