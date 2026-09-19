# Random library
import random

# number = random.random()

# print(number)


# ls = ["Aman","Simran","Nipun"]
# winner = random.choice(ls)

# print("The Winner Is: ",winner)

# dice = random.randint(1,6)

# print("You Have Rolled The Number: ",dice)

# import math

# square_root = math.sqrt(4)

# print(square_root)


# R.P.C
# choice = random.choice
# user_input = input("What Whould You Like To Pick? ")
# options = ["rock","paper","scissors"]

# if user_input == options[0]:
#     choice(options)
#     if choice(options) == user_input:
#         print("Its A Draw, Play Again.")
#     if user_input == options[0] and choice(options) == options[1]:
#         print("The AI Wins")
#     else:
#         print("The User Wins YAY")

# if user_input == options[1]:
#     choice(options)
#     if choice(options) == user_input:
#         print("Its A Draw, Play Again.")
#     if user_input == options[1] and choice(options) == options[2]:
#         print("The AI Wins")
#     else:
#         print("The User Wins YAY")

# if user_input == options[2]:
#     choice(options)
#     if choice(options) == user_input:
#         print("Its A Draw, Play Again.")
#     if user_input == options[2] and choice(options) == options[0]:
#         print("The AI Wins")
#     else:
#         print("The User Wins YAY")
        
# Gamba Simulator
numbers = random.randint(1,2)
user_input = int(input("Guess The AI's Guess: "))

if user_input == numbers:
    print("Good! You live to see another day")
else:
    print("Just perish Already.")