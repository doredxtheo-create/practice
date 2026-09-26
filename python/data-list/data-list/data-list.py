# fruits_before = ["apple","banana","cherry"]

# print(fruits_before)

# fruits_before.remove("cherry")

# print(fruits_before)

# Assignment 1: Nested Lists

# l = ""

# lists = [ l == ["cherry", "apple", "banana"]]

# print(len(lists[0]))

ls = []

nums = [1,2,3,4,5,6,7,8,9]

print("The Value Of Numbers Are: ",nums)

nums = nums[::-1]

print(nums)                

print("Every Number Multiplied by 3 is: ")


def match_words(words):
    counter = 0
    ls = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter += 1
            ls.append(word)
    return counter
count = match_words(["abc","cfc","xyz","aba","1221","AshA"])
print("The Number Of Words having first and last letters same are: ",count)

