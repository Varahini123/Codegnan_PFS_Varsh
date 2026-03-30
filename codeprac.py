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






























