print("Please select The Operation: ")
print("\n1. Addition")
print("\n2. Subtraction")
print("\n3. Multiplication")
print("\n4. Division")
choice = int(input("\nEnter Your Choice: "))

if choice == 1:
    def addition(x,y):
        return x + y

    z_1 = int(input("Enter the first number: "))
    Z_2 = int(input("\nEnter the second number: "))

    result = addition(z_1, Z_2)

    print("The Value Of The Result Is: ",result)

if choice == 2:
    def subtraction(x,y):
        return x - y

    z_1 = int(input("Enter the first number: "))
    Z_2 = int(input("\nEnter the second number: "))

    result = subtraction(z_1, Z_2)

    print("The Value Of The Result Is: ",result)

if choice == 3:
    def multiplication(x,y):
        return x * y

    z_1 = int(input("Enter the first number: "))
    Z_2 = int(input("\nEnter the second number: "))

    result = multiplication(z_1, Z_2)

    print("The Value Of The Result Is: ",result)

if choice == 4:
    def division(x,y):
        return x / y

    z_1 = int(input("Enter the first number: "))
    Z_2 = int(input("\nEnter the second number: "))

    result = division(z_1, Z_2)

    print("The Value Of The Result Is: ",result)

