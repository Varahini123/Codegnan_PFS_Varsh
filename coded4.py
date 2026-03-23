'''
#if statement 
#if-else statement
#if-elif-else statement
'''
#if statement --->this(if statement)is used to check any condition, if the condition becomes true then it will enter in side the (if statement)
'''
age = int(input("Enter your age: "))
if age >=18:
    print("your age is 18 or above")
student_att = int(input("Pls enter your sem attendance: "))
if student_att >= 75:
    print("you can directly sit in the sem exam")
'''
'''
employee_sal = int(input("enter your salary: "))    
if employee_sal >= 10000:
    print("You can save upto 5000")
'''

#if-else statement --->else part is called as fall-back statement. it only executes when the(if statement) is false
'''
age = int(input("Enter your age: "))
if age>=18:
    print("you can vote")
else:    
    print(f"your cannot vote and have to wait{18-age}years")
'''
'''
total_amount=int(input("Enter the total shopping money: "))
if total_amount>=149:#if keyword (condition):
    print("you get free delivery")
else:
    print(f"you get free delivery if you add{149-total_amount} to your cart")
'''
#if-elif-else statement(if+else)--->in the elif part, I can check one more condition
'''
student_marks = int(input("Enter your marks: "))
if student_marks >= 90:
    print("You got A+ grade")
elif student_marks >=75 and student_marks <90:
    print("you got A grade")
elif student_marks >=60 and student_marks <75:
    print("you got B grade")
else:
print("Your fail")
'''
'''
number_1=int(input("Enter 1st number: "))
number_2=int(input("Enter 2nd number: "))
user_choice = input("Enter user choice")
if user_choice =="+":
    print("the sum is: " ,num_1+num_2)
elif user_choice =="-":
    print("the difference is: ",num_1-num_2)
elif user_choice == "*":
    print("the product is: ",num_1*num_2)
'''

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
user_choice = int(input("enter your choice \n1.Add \n2.Sub \n3.Mul \n4.Div: "))
if user_choice == 1:
    print(num_1 + num_2)
elif user_choice == 2:
    print(num_1 - num_2)
elif user_choice == 3:
    print(num_1 * num_2)
elif user_choice == 4:
    print(num_1 / num_2)
    

    




    

    
        
    
    
    
    
