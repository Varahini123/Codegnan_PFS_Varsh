'''#functions()--> function is a block of code which is reusable an only runs when it is called
#it can return data as a result
#it helps avoiding code repetitions
#two types-->1. Built-in or in-build and 2.User define
             
1.Built-in or In-build
------------------------
--->they comes with the program itself and thise are already defined.....
eg..
print(),sum(),map()....

2.User dfine
-------------------------
--->this is created by person who is developing or usingfor development.
NOTE-->it starts with a def keyword followed by function name.
    -->and it has calling function....

syntax-->
def func_name():--->"()inside these brackets are parameters"
    xxxxxxxxx
    xxxxxxxxx
    xxxxxxxxx
    xxxxxxxxx
func_name()

'''

'''
#even number#
a = 10
num = int(input("enter a number: "))
def num_even_odd(a):
    if a % 2 == 0:
        print(f"{a}it is even")#arguements can be changed and it considers arguements value only
    else:
        print(f"{a}it is odd")
num_even_odd(a=2)
'''

'''
prime_num = int(input("enter a number: "))
count = 0
def prime_check(num,k):
    for j in range(1,num+1):
        if num % j == 0:
            k += 1
    if k == 2:
        print("prime")
    else:
        print("not")
prime_check(prime_num,count)
'''


rev_str = "madam" 
empty_ = ""
def palindrone_check(rev_str,empty_):
    for j in rev_str:
        empty_ = j + empty_      #for reversing the value use this method instead of using -1 collan method 
    if empty_ == rev_str:
        print(f"{rev_str} is palin")
    else:
        print(f"{rev_str} is not a palin")
palindrone_check(rev_str,empty_)













































