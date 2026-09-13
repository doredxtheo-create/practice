# How to form a TypeError

# age = 15
# print("Age Is: "+ age)

# How to form a NameError

# print(age1)

# How to form a SyntaxError

# def leg()

# How to form a ValueError

# age = int("hello")

# How to form a ZeroDivisionError

# def div():
#     return(100/0)

# return_value = div()

# How to form a IndexError

# num = [0]

# print(num[3])




# Assignment 1: ValueError

try:
    inp = int(input("Enter a number: "))
# print("the Number is: "+ inp)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print("The Number is: " + str(inp))

# Assignment 2: ZeroDivisionError
try:
    n1,n2 = eval(input("Enter two numbers: "))
    result = n1/n2
    print("The Result is: "+ str(result))
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Invalid Input Has Been Used, Please Only Use Two Numbers Separated By A Comma.")
except:
    print("An unexpected error occurred.")
else:
    print("The Result is: " + str(result))
finally:
    print("leg")

