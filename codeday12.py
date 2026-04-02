'''
#Break --->this is used to exit from the loop ,when we found the required element/value...
#example-->

for j in range(1,10):
    print(j)
    if j == 5:
    break
'''
'''
lis_ = [1,2,3,4]
for n in lis_:
    print(n)
    if n == 3:
        break
'''
'''
#Continue---->this is used to skip that particular loop which is mentioned in the conditiond where it cannot skip multiple numbers as well 

for j in range(1,10):                                                                                          
    if j == 5:
        continue
    print(j)

o/p--
1
2
3
4--skips '5'
6
7
8
9


for j in range(1,10):
    if j == 5 & j ==7:
        continue
    print(j)

 o/p        
1
2
3
4
5--#it cannot skip multiple numbers
6
7
8
9

lis_ = [1,2,3,4]
for n in lis_:
    if n == 3:
        continue
    print(n)
'''

'''
#pass--->this is called as space holder
incase any statement like(if,for,else,elif...)this should not complete, if not we will get syntax error to avoid this,we use pass

for j in range(1,100):
    pass
'''

'''
#else -- for
------------
it will fall back to else block, when all loops are completed

for m in range(1,10):
    print(m)
else:
    print("else block")
'''

'''
#while loop---> this is the combination of 'if' and 'for' statements,if we did not end the loop in proper way it will run upto the memory space in the sysytem
num = 1
while num<5:
    print(num)
    num += 1
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
    
    































