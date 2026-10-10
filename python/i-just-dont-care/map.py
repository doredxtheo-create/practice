# Assignment 1: Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = list(map(lambda x, y: x + y, list1, list2))
print("Addition of numbers from two lists:", result)

# Zip function example

names = ["Alex", "Bob", "Charlie", "David", "Eve"]
marks = [85, 90, 78, 92, 88]
result = list(zip(names, marks))
print("Names and their corresponding marks:", result)

for i,j in zip(names, marks[::-1]):
    print(f"{i} scored {j} marks.")
    # print(i,j)
    
for i in range(1,11):
    if i == 5:
        print(exit)
        exit()
    print(i)