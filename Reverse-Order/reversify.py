# Story: Harshit is a very curious kid. He is always trying to create something new. For example, he has an idea to design a program that will help count the digits in a number this time.

# Steps:

#• Make a sequence of steps to achieve the goal.
#• Feel free to use different blocks of code to make the project
# more interesting.
#• Close any pop-up/dialogue window that comes up during
# the project.
#• Finally, note down the doubts that you might have faced
# during the project.

number = input("Enter a number: ")

reverse = ""
for char in number:
    reverse = char + reverse

reversed_number = int(reverse)

print("The reverse order of", number, "is", reversed_number)

print("CHECKMATE")
exit(0)
