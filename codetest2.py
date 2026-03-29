'''
text = "Python is a programming language and has a lot of datatypes and methods to create codes"
print(f"the length of the sentence is:{len(text)}")#using f string function to count the length
count_vowels = 0
count_consonants = 0
count_spaces = 0
text_lower = text.lower()
vowels = ('AEIOUaeiou')#tuple
vowel_set = set(vowels)#set
for j in text:
    if j in vowel_set:
        count_vowels += 1
print(f"In this sentence the vowels counts is:{count_vowels}")
for j in text:
    if j is not 'vowels_set' and j not in " '.,@&#^%*":
        count_consonants += 1
print(f"In this sentence the consonants counts is:{count_consonants}")
for j in text:
    if j in " ":
        count_spaces += 1
print(f"In this sentence the spaces counts is :{count_spaces}")
'''


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
































































