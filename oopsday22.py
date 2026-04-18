'''
#constructor(__init__)-->A constructor is special method whhich is used to intialise object data.
#example-->
#__init__
-------------
class car:                          #here car is the class
    def __init__(self,brand,color): 
        self.brand = brand
        self.color = color
car_1 = car("Toyota","black")
car_2 = car("Thar","white")
print(car_2.brand,car_2.color)


#name&branch
class student:                          
    def __init__(self,name,branch): 
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name,self.branch)
student_1 = student("hema","CSE")
student_1.display()

#mycoursename , days
class myself:
    def __init__(self,course,days):
        self.course = course
        self.days = days
    def display(self):
        print(self.course,self.days)
mycourse_1 = myself("python full stack","4months")
mycourse_1.display()'''

'''
#Access Specifiers
-------------------
1.Public
Syntax -- name
we use anywhere in the program

2.Protected
Syntax -- _name
this is only for internal use

3.Private
Syntax -- __name
this is restricted

4.self
this is keyword is instance variable and unique for each object

class some:
    def __init__(self):
        self.public="Public"
        self.protected="Protected"
        self.privatev="private"
any = some()
print(any.public)
print(any.protected)   #'__'before name keeps it private...if want public to see the info no'__'
print(any.__private)'''

'''

user_acc_details = {"Name": "Hema", "ATM pin": "8074", "Balance": 70000, "Transaction History": []}
print("welcome to Union Bank ATM")
print("please insert your card")
pin = input("enter your 4-digit pin: ")
if len(pin) == 4:
    if pin == user_acc_details['ATM pin']:  
        user_choice = int(input("enter \n 1.Withdraw: \n 2.Deposit \n 3.Pin change \n 4.Transaction History\n"))
        if user_choice == 1:
            money_w = int(input("enter the amount you want to withdraw: "))
            if money_w <= user_acc_details['Balance']:
                user_acc_details['Balance'] -= money_w
                user_acc_details['Transaction History'].append(f"Withdrawn: {money_w}")  
                print(f"Withdrawal successful. Balance: {user_acc_details['Balance']}")
            else:
                print("insufficient balance")
        elif user_choice == 2:
            money_d = int(input("enter the amount you want to deposit: "))
            if money_d % 100 == 0 and money_d >= 5000:
                user_acc_details['Balance'] += money_d
                user_acc_details['Transaction History'].append(f"Deposited: {money_d}")
                print(f"Deposit successful. Balance: {user_acc_details['Balance']}")
            else:
                print("the money cannot be deposited")
        elif user_choice == 3:
            attempts = 3
            while attempts > 0:
                old_pin = input("enter your old_pin: ")
                if len(old_pin) == 4:
                    if old_pin == user_acc_details['ATM pin']:
                        new_pin = input("enter the new pin: ")
                        if len(new_pin) == 4 and old_pin != new_pin:
                            user_acc_details['ATM pin'] = new_pin  
                            print("PIN changed successfully. New pin is:", new_pin)
                            break
                        else:
                            print("Invalid: PIN must be 4 digits and different from old PIN")
                    else:
                        attempts -= 1
                        print(f"you entered incorrect pin and you have {attempts} left")
                        if attempts == 0:
                            print("your card is blocked")
                else:
                    print("enter 4 digit pin")
        elif user_choice == 4: 
            if user_acc_details['Transaction History']:
                print("Transaction History:")
                for transaction in user_acc_details['Transaction History']:
                    print(transaction)
            else:
                print("No transactions yet")
        else:
            print("Invalid option")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")'''

















































































