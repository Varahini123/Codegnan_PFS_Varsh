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

Multi-level-->this occurs when a class inherits from a child class,creating a grandparent->parent->child in this structure.

class Grandparent:
    def Show_GrandParent(self):
        print("I'm Grandparent")

class Parent(Grandparent):
    def Show_Parent(self):
        print("I'm Parent")  

class child(Parent):
    def Show_child(self):
        print("I'm child")





#mobileupdate
class BaseApp:
    def Show_BaseFeatures(self):
        print("Base features: Login, Home Screen, Notifications")

class UpdatedApp(BaseApp):
    def Show_NewFeatures(self):
        print("theme: Dark Mode, Chat Support")

class LatestVersionApp(UpdatedApp):
    def Show_LatestFeatures(self):
        print("Add updates: AI Chat, UPI Payments, Offline Mode")

my_app = LatestVersionApp()
my_app.Show_BaseFeatures()      
my_app.Show_NewFeatures()       
my_app.Show_LatestFeatures()    


Hierarchical inheritance-->this occurs when one parent class has multiple child classes inherits, this process is called heirarchical

example:-
class parent:
    def Parent_(self):
        print("I'm Parent")
        
class child_1(parent):
    def child_(Self):
        print("I'm 1st child")
        
class child_2(parent):
    def _child(self):
        print("I'm 2nd child")
        
class child_3(child_1, child_2):
    def child(self):
        print("I'm the child")

thing = child_3()
thing.Parent_()
thing.child_()
thing._child()
thing.child()

Hybrid inheritance-->this is a combination of two or more types of inheritance, such as sing.
multiple,multi-level, or hierachical all this in a single class.


class Grandparent:
    def Show_GrandParent(self):
        print("I'm Grandparent")

class Parent(Grandparent):
    def Show_Parent(self):
        print("I'm Parent")  

class child(Parent):
    def Show_child(self):
        print("I'm child")

any = child()
any.Show_GrandParent()
any.Show_Parent()
any.Show_child()
class parent:
    def Parent_(self):
        print("I'm Parent")
        
class child_1(parent):
    def child_(Self):
        print("I'm 1st child")
        
class child_2(parent):
    def _child(self):
        print("I'm 2nd child")
        
class child_3(child_1, child_2, Grandparent):
    def child(self):
        print("I'm inherited from Grandparent class and child_1, child_2")

thing = child_3()
thing.Show_GrandParent()
thing.Parent_()
thing.child_()
thing._child()
thing.child()'''



    


































