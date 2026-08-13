# For Example: (Assignment 1) 

n = int(input("Enter The Number whose sum whom we want to find: "))
# 5 -> 1+2+3+4+5 = 150 ;
sum = 0

for i in range(1, n+1):
    sum = sum + i
print("The sum of numbers from 1 to", n, "is:", sum)


# Assignments 2: (String Reverse)

user_input = input("Enter A String To Reverse: ") # leg
reverse = ""
for char in user_input:
    reverse = char + reverse
print("The reversed string is:", reverse)

# Number Reverse

n = 10

for i in range(10,0,-2):
    print(i)

# "Take No. from user and print from that no. down to 1" -> Ass-1 

# Assignment -2: Print no.s from 20 to 10 in reverse order.


# Complete Ass-1:\\

User_Input = int(input("Enter a number to print from that number down to 1: "))
for i in range(User_Input, 0, -1):
    print(i)

# Complete Ass-2:\\

for i in range(20, 10, -1):
    print(i)

exit(0)


