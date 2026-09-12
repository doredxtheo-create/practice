# # imaginary name Keywords.py :)

# # list of keywords in python
# # keywords = [
# #     "False",
# #     "None",
# #     "True",
# #     "and",
# #     "as",
# #     "assert",
# #     "async",
# #     "await",
# #     "break",
# #     "class",
# #     "continue",
# #     "def",
# #     "del",
# #     "elif",
# #     "else",
# #     "except",
# #     "finally",
# #     "for",
# #     "from",
# #     "global",
# #     "if",
# #     "import",
# #     "in",
# #     "is",
# #     "lambda",
# #     "nonlocal",
# #     "not",
# #     "or",
# #     "pass",
# #     "raise",
# #     "return",
# #     "try",
# #     "while",
# #     "with",
# #     "yield",
# # ]


# # I googled the keywords in python and found this list.




# # Assignment 1: Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.” using break statement.

# string = input("Enter a string: ")
# for char in string:
#     if char == "A":
#         print("Alphabet 'A' is present in the string.")
#         break
# else:
#     print("Alphabet 'A' is not present in the string.")


# # Assignment 2: Pass;  Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.
# for i in range(1, 101):
#     if i % 20 == 0:
#         print("twist")
#     elif i % 15 == 0:
#         pass
#     elif i % 5 == 0:
#         print("fizz")
#     elif i % 3 == 0:
#         print("buzz")
#     else:
#         print(i)


# def call():
#     return("leg")

# print(call())



# # assignment 4: Lets try out pass statement.

# # def leg():
# #     pass    

# # print("I am Smart")


# a = input("Enter a Word: ")

# for i in (a):

#     if i == 'A':
#         print("The Alphabet 'A' is present in the given word.")
#         break
#     else:
#         print("The Alphabet 'A' is not present in the given word.")
#         break


# Assignment 5:

for x in range(10):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print(x)




