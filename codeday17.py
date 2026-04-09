'''lambda function()
-->this is also called anonymous function.
-->a lambda function can take n number of arguements but they have one expression
-->syntax-
         lambda(keyword) arguments : expression

any = lambda so : so + 10
print(any(6))

str = lambda a,b:b - a          #here we can give any number of arguments but the exp should be in one format
print(str(4,9))


str = lambda an, how, do : (how - an)/do          #here we can give any number of arguments but the exp should be in one format
print(str(4,9,5))                                     #an is 4,how is 9,do is 5


num = lambda e : e - 45
print(num(5))

some = lambda they , an , so : (they-an)*so
print(some(20,93,34))

List comprehension:
-----------------
-->this offers the shorter syntax when you want to create a new list from the existing list.
-->syntax-
         variable_name = [expression loop or condition]


pre_list = [24,37,99,57,21]
new_list = [j for j in pre_list]      #'j' for, is an expression which helps to save in the list
print(new_list)


pre_list = [24,37,99,57,21]
new_list = [j for j in pre_list if j%2==0]      #even numbers printing
print(new_list)'''






















