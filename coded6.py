'''
#printing vowels and cosonants
vowel_con = input("Enter a letter")
if vowel_con is "AEIOUaeiou":
    print("vowel")
else:
    print("consonant")

'''
'''
time_aday = input("Enter 24 hours time: ")
parts_ = time_aday.split(":")
hours_ = int(parts_[0])
mins_ = int(parts_[1])
if hours_ >=13 and mins_ <60:
    print(f"{time_aday}convert into {hours_ -12}:{mins_}pm")
else:
    print(f"the entered time is already in the 12hr clock are incorrect")
'''

'''
#24hrs into 12hrs

time_aday = input("Enter 24 hours time: ")
parts_ = time_aday.split(":")
print(parts_)
hours_ = int(parts_[0])
mins_ = int(parts_[1])
print(hours_)
print(mins_)
if hours_ >=13 and mins_ <60:
    print(f"{time_aday}convert into {hours_ -12}:{mins_}pm")
else:
    print(f"the entered time is already in the 12hr clock are incorrect")
'''

'''
#lists-Collection of different datatypes inside the [] , which are seperated by ','
------------------

example --
[1,"Name",[1,2,"hema"]]


List_1 = [1,2,3,"python",[1,2,["python","java"],"language"]]
print(f"the letter {List_1[4][2][0][3]}") #count every bracket as a list and name it accordingly so that to print the single letter                         
print(List_1[4][2][1][0])

'''


'''
#methods of lists
---------------

#append()---this method is used to add new item into list it will only go for the last index of the list it can be int or strings
syntax--> variable_name.append("item")

#extend()--- this method is used to add items to the list in the last index only as a extension,where each item or substring is each index in the list
syntax---> variable_name.extend("item")

#remove()--->this method will delete the item or value directly from the list
syntax--> variable_name.remove("item")

pop()--- this method will delete the item or value based on index position
syntax---> variable_name.pop(


mutable -->in this i can directle modify in a particular variable
immutable--->in this i could not able to perform any particular variable


#append example
list_2 = [1,2,3,4,5]
print(list_2)
list_2.append(56)
print(list_2)
list_2.append("hema")
print(list_2)
list_2.append("[1,2]")
print(list_2)

'''

'''
#extend() example

list_3 = [34,45,23,44]
print(list_3)
list_3.extend("hema")
print(list_3)
list_3.append("[0.3]")#float alone cannot be added to the extension... it can be joined only when added with int to list
print(list_3)
'''


'''
#remove() example

list_4 = [34,22,45,2]
print(list_4)
list_4.remove(45)
print(list_4)
list_4 = [34,22,"python", 45,2]
list_4.remove("python")
print(list_4)

'''

'''
#pop() example

list_5 = [23,"hema",33,46,34]
list_5.pop(1)
print(list_5)

'''












































































































