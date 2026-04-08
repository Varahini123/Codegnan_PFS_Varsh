'''#ways to pass arguments in calling func
#required arguments
--------------
-->it should match same number variables in calling with def

num = 9
num_2 = 10
def add(num,num_2):
    print(num+num_2)
add(num,num_2)

#default arguments
----------
-->it will take the default values from the arguments


my_name = "hema"
def add(my_name):
    print(my_name)         #by default the name given here takes "varshini and kakara"  
add(my_name = "varshini")
add(my_name = "kakara")


num = 9
count = 0
def prime(num,count):
    for i in range(1,num+1):
        if num % i == 0:
            count += 1               #checking prime for multiple numbers
    if count==2:
        print(f"{num} it is prime number")
    else:
        print(f"{num} it is not prime number")
prime(num=41,count=0)
prime(num=9,count=0)      #keyword arguments

            
def any(num,num_3,num_2):
    print(f"num = {num},num_2 = {num_2},num_3 = {num_3}")
any(num_2=7,num=0,num_3=90)


#variable length arguments-
#adding a star(*)before the parameter name in func,receive a tuple of arguments and can access items with indices


def name(*student):      #*-->assigning values in the form of tuples
    print(student)
name("divya","sree","priya")

'''






























