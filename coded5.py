'''#strings--->this is sequence of characters or collections which comes anything in single coats(' ' )or double coats(" ")
we can access the string using indexing(string can also allow negative indexing) and also slicing(means to cut the string into pieces )
any = '123'(anything btwn single coats are strings)
'''
'''
any = 'Hema Varshini'
print(any[7:13])  #finding the index placement in the words
# string indices must be integers, not 'tuple'
#coolen gives from one placed index to another
'''

'''
any = 'Hema Varshini'
print(any[-6])
#so = any.replace("Hema","Java")
#print(so) #this is also immutable,where i could not be able to modify that particular variable
#print(any)
len()-->len method is used to get the characters present in the strings or find the length of the string
'''

'''
any = 'Hema Varshini'
print(any[20])#string index out of range it could not access the indexing placement
'''


'''
any = 'Hema Varshini'
print(any)
a_day ="I'm hema and i came from vizag taking a python course"
print(f"my name is {a_day[4:8]}")
print(f"my course {a_day[-13:-7]}")

data = "Hema"
print(data[: :-1])# to print the index in reverse order

a_day ="I'm hema and i came from vizag taking a python course"
print(a_day[: :-2])
#note:-we can able to convert a string into integers only if the string contain only integer value(str = '123'----example
                                                                                                  num = int(str)
                                                                                                  print(type(num)))

'''


'''
data = '123'
print(type(data))#to find the length of the string
print(len(data))


str = '123'
num = int(str)
print(type(num))
'''

'''
#methods of string
-------------------
split()--->removes space, and then that is the list[]it will give the seperated thing in each index
syntax:- variable_name.split("substring")

lower()--->this is used to convert all letters into lowercase
syntax--->variable_name.lower()
upper()--->this is used to convert all letters into uppercase
syntax--->variable_name.upper()

'''

'''
#shows the spaces and gets seperated for every word
some = "python is a  programming language"
print(some.split())


some = "pytho is a  programming language"
print(some.split("programming"))

#to get the given variable with the taken upper or lower case when the str has any case
str = "pythON is A prograMMing language"
print(str.lower())
print(str.upper())

some = "python is a programming language"
if "A" in some:
    print("Yes, it is there")
else:
    print("No, it is not there")


#replace()--->

#syntax---> variable_name.replace("old string","new string")
some = "Python is a programming language"
print(some.replace("programming","normal"))
'''

some = "python is a programming language"#to check the string
if "is" in some:
    print("yes , it is there")
else:
    print("no, it is not there")


some = "python is a programming language"#to check the string
if "ython" in some:
    print("yes , it is there")
else:
    print("no, it is not there")#shows the output in the sequence .. if breaks no























