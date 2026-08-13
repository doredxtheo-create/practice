# Vrisha is very good at maths. But her friends always get stuck whenever there is power calculation. They feel it is too lengthy, and too much calculation is required to solve the problem. So, to help her friends, she designed a program where users can calculate n number of power of the given number.

base = int(input("Enter the base number: "))
n = int(input("Enter how many powers you want to calculate: "))

for i in range(1, n + 1):
    print(f"{base}^{i} = {base ** i}")

print("CHECKMATE")
