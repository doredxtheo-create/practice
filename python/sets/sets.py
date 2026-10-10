from array import array as arr

# Sets are Unoredered collections of unique elements. They are mutable, meaning you can add or remove elements after the set has been created. Sets are useful for membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, difference, and symmetric difference.

# Arrays In Python are implemented using the built-in set data type. Sets can be created using curly braces {} or the set() constructor.


numbers = {1, 2, 3, 4, 5}
# Find Position of an Element in a Set

for element in numbers:
    print(element)
    
# Now Take Differnt Types of Elements in a Set.

satelite = {"Earth", 24, 3.14159, True}
for element in satelite:
    print(element)
    
    
def catagorization():
    x = input("Enter Any Value,String,Float or Booolean: ")
    if x in satelite == 1:
        print("Yes, This Value is Present in the Set")
    else:
        print("No, This Value is Not Present in the Set")
    if x in satelite == 24:
        print("Yes, This Value is Present in the Set")
    else:
        print("No, This Value is Not Present in the Set")
    if x in satelite == 3.14159:
        print("Yes, This Value is Present in the Set")
    else:
        print("No, This Value is Not Present in the Set")
    if x in satelite == True:
        print("Yes, This Value is Present in the Set")
    else:
        print("No, This Value is Not Present in the Set")
        
        
# Create Var. = mind_set

my_set = set([1, 2, 3, 4, 5])

print(my_set)
x = int(input("Enter Any Value to Check if it is Present in the Set: "))
print(x in my_set)  # Returns True if the value is present, otherwise False


# Use Pop method to Remove an Element from a Set

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.pop()  # Removes and returns an arbitrary element from the set
print(my_set)  # Output: {1, 3, 4, 5} (the element 2 is removed)

# Create 2 Sets

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

result = set_1.union(set_2)  # Union of two sets
print(result)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Use Intersection Method to Find Common Elements in Two Sets

result = set_1.intersection(set_2)
print(result)  # Output: {4, 5}

# Use Count Method to Count the Number of Elements in a Set

arr_numbers = arr('i', [1, 2, 3, 4, 5])
print(str(arr_numbers.count(3)))  # Output: 1

# count = len(arr_numbers)

count = len(arr_numbers)
print("The Number of Elements in the Array is:", count)  # Output: The Number

# Use Reverse Method

arr_numbers.reverse()
print("The Reversed Array is:", arr_numbers)  # Output: The Reversed Array

# Append Method to Add an Element to the Array

arr_numbers.append(0)
print("The Array after Appending 0 is:", arr_numbers)  # Output: The Array after Appending 0 is: array('i', [1, 2, 3, 4, 5, 0])

# Use Insert Method to Add an Element at a Specific Position in the Array
arr_numbers.insert(2, 10)  # Inserts 10 at index 2
print("The Array after Inserting 10 at Index 2 is:", arr_numbers)  # Output: The Array after Inserting 10 at Index 2 is: array('i', [1, 2, 10, 3, 4, 5, 0])
