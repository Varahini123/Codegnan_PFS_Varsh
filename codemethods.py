#list methods
#A list in Python is a collection of items stored in a single variable.

# Create a list
nums = [1, 2, 3]

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
