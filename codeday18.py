'''#generator-->this a special type of function that generates (or) return an ITERATOR which one at a time

#basic program
def my_gen():
    yield 1
    yield 2     #"yield" is nothing but the term as"return" in func.yeild will pause and resume
    yield 3
    yield 4
my_gen1=my_gen()
print(next(my_gen1))
print(next(my_gen1))
print(next(my_gen1))
print(next(my_gen1))

#squares
def square_gen(n):
    for i in range(n):
        yield i*i
for val in square_gen(9):
    print(val)

#Yield-->it will take a pause and again resume, this is not a normal keyword cannot be used in the func.
#this is used to produce a value and pause execution.

#Next()-->this is used to get next value from a generator
#when the value is finised , it will stop the iterator

#power **
def power_gen(n):
    for i in range(n):
        yield i**i
for val in power_gen(9):
    print(val)

#subraction
def sub_gen(n,m):
    for i in range(n):
        yield n - m
sub_gen1=sub_gen(99,22)
print(next(sub_gen1))

#division
def div_gen(a,b):
        yield a/b
div_gen1=div_gen(99,22)
print(next(div_gen1))

#even odd 
def evn_odd_num(n,m):
    if n%2==0:
        yield"even"
    else:
        yield"odd"
evn_odd_num1=evn_odd_num(22,21)
print(next(evn_odd_num1))

#generating numbers one next to another       
def num_gen(n):
    for i in range(n):
        yield i
for val in num_gen(101):
    print(val)'''

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


























































