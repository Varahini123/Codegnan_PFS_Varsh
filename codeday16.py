'''
#Recurrsion is a programming techniques where a func calls itself either directly or indirectly to solve a problem by breaking it into
smaller,simpler subproblems. Recurrsion is especially useful for problems that can be divided into identical smaller tasks such as mathematical
calculations,tree traversals or dive and conquer algoeithms.'''

'''
def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("enter 4 digit PIN: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("✅Welcome to the ATM")
            return True
       else:
        self.remaining_attempts -=1
        if self.remaining_attempts > 0:
            print(f"❌ Invalid PIN. Attempts left: {self.remaining_attempts}")
        else:
            print("⭕card blocked . please contact customer service")
            return False'''

'''
str_any = "Python is a programming language"
vowel_list = []
Consonants_list = []
def vowel_con(any,vowel_list,Consonants_list):
    for j in str_any:
        if j in "AEIOUaeiou":
            vowel_list.append(j)
        else:
            Consonants_list.append(j)
    print(f"{vowel_list} these are all vowel in the string")
vowel_con(any,vowel_list,Consonants_list)
'''    
    
'''
num = 7
def prime_num(num):
    for j in range(1,num+1):
        if num%j == 0:
            count+=1
        if count == 2:
            print(f"{num}it is prime)
        else:
            print(f"{num} it is not prime)
prime_num(num)
'''
'''
ICIC_hema_ = {"Name" : "Hema","ATM PIN" : "8074","Balance" : 5000}
user_pin = input("enter 4 digit pin: ")
if len(user_pin) == 4:
    if user_pin in ICIC_hema_['ATM PIN']:
        user_choice = int(input("enter \n1.Withdraw: \n2.Deposite"))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw: "))
            if money_w <= ICIC_hema_['Balance']:
                ICIC_hema_['Balance'] -= money_w
                print(ICIC_hema_['Balance'])
            else:
                print("insuff")
        elif user_choice == 2:
            money_d= int(input("enter the amount you want to deposite: "))
            if money_d%100==0 and money_d>=5000:
                user_acc_details['balance']+=money_d
                print(user_acc_detials['Balance'])
            else:
                print("the money cannot be deposited")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")
'''








































