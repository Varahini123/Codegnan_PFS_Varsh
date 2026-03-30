'''
text = "My name is kakara hema varshini from vishakapatnam AP. Currently I'm taking a full stack course in python ar Codegnan Institute. I completed my bachelor's of degree from Dr lankapalli bullaya college of engineering from Computer science department and I'm a recent graduate passed out in 2025 year . I am now confident in using python coding in IDLE work shell on using few methods like lists , tuples , sets, dictionary etc ."
print(f"the length of the paragraph is:{len(text)}")#using f string function to count the length
count_vowels = 0
count_consonants = 0
count_spaces = 0
text_lower = text.lower()
vowels = ('AEIOUaeiou')#tuple
vowel_set = set(vowels)#set
for j in text:
    if j in vowel_set:
        count_vowels += 1
print(f"In this paragraph the vowels counts is:{count_vowels}") 
for j in text:
    if j is not 'vowels_set' and j not in " '.,@&#^%*":
        count_consonants += 1
print(f"In this paragraph the consonants counts is:{count_consonants}")
for j in text:
    if j in " ":
        count_spaces += 1
print(f"In this paragraph the spaces counts is :{count_spaces}")

'''

'''
#"j" is an initial variable where it cannot show any error in the output that varaible itself is self initialized where it can shown anytime
#the diff is -normal varaible has to be defined

a = 9
print(b)#name 'b' is not defined-->error for normal varaiable
for j in range(1,10):
    print (j)

'''
'''
Range()--->this is used to generate numbers
syntax---->range(start,end,step)#it stops with every step given in the number it indicated the position not the number
example --

for j in range(1,20,3):
    print(j)
output:-
1
4
7
10
13
16
19
'''
'''
any = "123"
print(list(any))#list gives the output seperating every variable
print(tuple(any))#tuple gives the output seperating every variable
print(str(any))


so = 123
print(str(so))#changing one datatype to another 
print(float(123))

'''

'''
an = [1,2,3]
vs = (str(an))
print(type(vs))
print(vs)
print(tuple(an))
'''

'''
rev_str = "madam"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_ #for reversing the value use this method instead of using -1 collan method 
if empty_ == rev_str:
    print(f"{rev_str}is palin")
else:
    print(f"{rev_str}is not a palin")
'''



















































































