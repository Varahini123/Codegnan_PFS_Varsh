'''
#indexing code
list_1 = [1,2,"hema","python",4,"language"]
print(list_1)
'''

'''
print(9+8)
print("Python"+"language")
print([1,2]+[3,4])

#concatenation
--------------
this is nothing but the plus symbol'+' behaving

case-1
--------
integers--this will act as addition for the integers

case-2
----------
for other datatypes (we have to use same type)this (+) acts as concadenation
errror -#if we try add two diff data types it cannot print the outputcan only concatenate str (not "list") to str or list to list
example--
"print("Hema" + [1,2])"


#str to str errors
print("hems" + [5+5])
#can only concatenate str (not "list") to str


#list to list error
print([3-2] + "python")
#can only concatenate list (not "str") to list
'''
'''
#Tuple
--------
tuple is a collection of different datatype these are represented by (), seperated by(,)

#example---
thing = (1,"hema",[12,4],(3,4))
print(thing)

#indexing
thing = (12,89,"python",(23,"hema",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(thing)        
print(thing[1])
print(thing[3][2][1][9])


#swapping the varaibles
num = 9
num_2 = 90
print(f"before swapping num = {num} and  num_2 = {num_2}")
num,num_2 = num_2,num
print(f"after swapping num = {num} and num_2 = {num_2}")

str = hema
str_2 = varshini
print(f"before swapping str = {str} and str_2 = {str_2}")
str,str_2 = str_2,str
print(f"after swapping str = {str} and str_2 = {str_2}")


leap_year = int(input("Enter year: "))
if (leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0):
      print(f"yes, {leap_year} is a leap year")
else:
    print(f"no, {leap_year} is not a leap year")
                
'''










































