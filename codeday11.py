'''
# generating tables
table_num = int(input("enter a number: "))
for j in range(1,11):
    print(f"{table_num} X {j} = {table_num * j}")
                    
'''

'''
#printing out the number of captital and small letter
an = "Python is a Programming language"
count_1 = 0
count_2 = 0
for ch in an:
    if ch.isupper():
        count_1 +=1
    elif ch.islower():
        count_2 +=1
print(f"There are total {count_1} Cap L")
print(f"There are total {count_2} small L")
'''

'''
an = "Python is a Programming language"
Cap_L = []
small_L = []
for ch in an:
    if ch.isupper():
        Cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f"{Cap_L} contain all Cap L")
print(f"{small_L} contain all small L")
'''

'''
ICIC_hema_AC_details = {"Name" : "Hema","ATM PIN" : "8074"}
print("Welcome to ICIC ATM")
print("Pls insert your ATM card")
ICIC_user_pin = input("Pls enter you 4 digit ATM pin: ")
if len(ICIC_user_pin) == 4:
    if ICIC_user_pin in ICIC_hema_AC_details['ATM PIN']:
        print("The pin is correct")
    else:
        print("You have entered invalid pin")
else:
    print("Pls enter 4 digit pin")
'''

'''
per_num = int(input("Enter a number: "))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect number")
else:
    print(f"{per_num} is not a perfect number")

'''






















































































