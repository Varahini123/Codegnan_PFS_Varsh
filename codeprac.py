'''
#reversing and palindrome check
rev_str = "madam"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_#for reversing the value use this method instead of using -1 collan method 
if empty_ == rev_str:
    print(f"{rev_str}is palin")
else:
    print(f"{rev_str}is not a palin")

'''
'''
#generating even numbers upto 100
for num in range(1,100):
    if num % 2 == 0:
        print(f"{num} is a even")
else:
        print(f"{num} is a odd")

'''




'''
for i in range(1, 101):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
'''

'''
even_numbers = []
odd_numbers = []   #SEPERATING EVEN AND ODD NUMBERS#

for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
'''


'''
even_numbers = []
odd_numbers = []
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} is an even number")
        even_numbers.append(i)
    else:
        print(f"{i} is an odd number")
        odd_numbers.append(i)
'''
'''
#generating fibanaci series with python
user_in = int(input("enter the limit: "))
num_1 = 0
num_2 = 1
print(num_1, num_2, end=" ")
for v in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")
'''



























