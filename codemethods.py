#list methods
#A list in Python is a collection of items stored in a single variable.

# Create a list
any = [1, 2, 3,a,b]

print("Original list:", nums)

# ----------- Adding elements -----------
nums.append(80)        # adds element at end
print("Append:", nums)

nums.insert(2, 30)     # inserts 15 at index 1
print("Insert:", nums)

nums.extend([55, 65])  # adds multiple elements
print("Extend:", nums)

# ----------- Removing elements -----------
nums.remove(20)        # removes specific value
print("Remove:", nums)

nums.pop()             # removes last element
print("Pop last:", nums)

nums.pop(1)            # removes element at index 1
print("Pop index 1:", nums)

# ----------- Searching -----------
print("Index of 30:", nums.index(30))  # finds index of element
print("Count of 10:", nums.count(10))  # counts occurrences

# ----------- Sorting & reversing -----------
nums.sort()            # sorts list in ascending order
print("Sorted:", nums)

nums.reverse()         # reverses list
print("Reversed:", nums)

# ----------- Copying -----------
new_list = nums.copy() # creates a copy of list
print("Copied list:", new_list)

# ----------- Clearing -----------
nums.clear()           # removes all elements
print("Cleared list:", nums)

#Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#-------------------------------------------------------------------------->
#Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#-------------------------------------------------------------------------->
#Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)  #output:['welcome', 'to', 'the', 'jungle']
#-------------------------------------------------------------------------->
#Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x) #output:Hello, and welcome to my world.
#-------------------------------------------------------------------------->
#Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)  #output: hello, and welcome to my world!
#-------------------------------------------------------------------------->
#Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)  #output:true
#-------------------------------------------------------------------------->
#Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x) #output:true
#-------------------------------------------------------------------------->
#other methods
#isdigit()
#isdecimal()
#islower()
#isupper()














































































