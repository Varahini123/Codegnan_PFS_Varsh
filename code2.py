'''
Variables -->Variables are named storage location that is used to hold data in
the memory,to make it simple it is the label which points out to a value -->
storage placeholders

Rules for defining variables
-->A-Z,a-z,0-9
-->start with uppercase,lowercase letters,even with a underscore_
-->But you cannot start with symbols (@,#,$,...), even numbers also

Better preferable way is go with general purpose -->you want to store your detials
name,email_id,account_number...

a=1
b=5
a=25
#python is dynamically typed,you need not define the datatype and also
#only the recent value to the variable with the same name is pointed

print(a)
print(b)

#1a23 = 24 #Syntax Error

#@werf = 4.5 #Syntax Error

#$dsf = 12 #Invalid Syntax

#Store your personal detials

name = "Codegnan"
location = "Visakhapatnam"
age = 7
emailid = "cmo@codegnan.com"
email_id = "cmo@codegnan.com"
print(name,location,age,email_id)

#How to assing multiple values to a variable
hema,likitha,divya = 21,20,23
print(hema)
print(likitha)
print(divya)

#assing same values to multiple variables

x = y = z = 21
print(x,y,z)

#Keywords are reserved words which will have specific useage
#There are 35 keywords in Python
#never use keywords as identifiers (ex- if=42 gives invalid syntax)

#if = 23
#lambda = 'saketh'
#False = 0 #cannot assing

#python is case-sensitive
false = 25

#Identifiers are names given to variables,functions,classes,object....

#Literals are fixed values to a identifier
age = 25
name = 'saketh'

#name is identifier,25 is literal

#Single line comments --> #
#Multiple lines comments uses 

#built-in datatypes -->numeric,boolean,collections

#Numeric datatypes -->it,float,complex
#int -->Specifically used for counting,values,quantity
#float -->Specifically used for temperature,percentage,price(rounding off)
#complex -->Specific conversions (real and imaginary)

count = 40
print(count)
print(type(count))

price = 175.25
print(price)
print(type(price))

j3 = 25
value = 2+j3
print(value)
print(type(value))

value = 2+3j
print(value)
print(type(value))

#Typecasting -->converting one type to another

#int -->float,complex

age = 25
print(type(age))

b = float(age)#creates another variable
print(b)
print(type(b))
c = complex(age)
print(c)
print(type(c))

#float,complex
print = 375.25
print(type(price))
d = int(price)
print(d)
print(type(d))
e = complex(price)
print(e)
print(type(e))

f = 2+5j
print(type(f))
#g = int(f) #complex to int is not varaible
#print(g)
h = float(f)#complex to float is not possible
print(h)
'''

'''
#boolean datatype -->validation -->True/False
a = True
print(a)
print(type(a))

#Typeconversion of bool
b = int(a)
print(b)
c = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))
'''
'''
#Input -->input()/ output -->print()
a = 5
print(a)
print(type(a))

a = int(input("Enter a value")) #any input but results as str
print(a)
print(type(a))

a = int(input("Enter a value:")) #only integer input
print(a)
print(type(a))

b = float(input("Enter another value"))
print(b)
print(type(b))
'''

#Now let's work on a simple case study using above -->Fee

#details of the students
name = input("Enter the student name:")
print("-------------")
admission_fees = int(input("Enter the Admission Fees:"))
tuition_fees = float(input("Enter the Tuition Fees:"))
hostel_fees = float(input("Enter the hostel Fees:"))
#Calculate the Total Fees
total_fees = admission_fees + tuition_fees + hostel_fees
print("<-------------->")
print("Student Name :",name)
print("Admission Fees is :",admission_fees)
print("Tuition Fees is :",tuition_fees)
print("Hostel Fees is :",hostel_fees)
print("Total Fees is = ",total_fees)
print("---------------")






















































