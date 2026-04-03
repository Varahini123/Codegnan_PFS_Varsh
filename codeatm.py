ICIC_hema_ = {"Name" : "Hema","ATM PIN" : "8074","Balance" : 5000}
user_pin = input("enter 4 digit pin: ")
if len(user_pin) == 4:
    if user_pin in ICIC_hema_['ATM PIN']:
        user_choice = int(input("enter \n1.Withdraw: "))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw: "))
            if money_w <= ICIC_hema_['Balance']:
                ICIC_hema_['Balance'] -= money_w
                print(ICIC_hema_['Balance'])
            else:
                print("insuff")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")
