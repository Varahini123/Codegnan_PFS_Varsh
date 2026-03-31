'''
#generating prime numbers
prime_num = int(input("Enter a umber:"))
count = 0
for j in range(1,prime_num+1):
    print(j)
    if prime_num % j == 0:
        count += 1
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")
'''

'''
for an in range(2,100):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count +=1
    if count == 2:
        print(f"{an} is a prime")
    else:
        print(f"{an} is not a prime")
'''

'''
list = [1057,197,9,86,17673] 
for an in list:
    print(an)
    count = 0
    for j in range(1, an+1):
        if an % j == 0:
            count +=1
    if count == 2:
        print(f"{an} is a prime")
    else:
        print(f"{an} is not a prime")

'''

'''
#append operator in removing duplicate value in list
any = [2,356,8,6,3,2,8]
empty = []
for j in any:
    if j not in empty:
        empty.append(j)
        print(empty)        
'''

'''
any = [2,356,8,6,3,2,8]
empty = []
for j in any:
    if j not in empty:
        empty.append(j)
    else:
        any.remove(j)
print(any)
                
'''

'''
so = int(input("enter any number: "))
length_ = len(str(so))
Amstr_ = 0
for j in str(so):
    Amstr_ +=int(j) ** length_
    print(Amstr_)
if Amstr_ == so:
    print(f"{so} is Amstrong num")
else:
    print(f"{so} is not Amstrong num")
'''



















































































































