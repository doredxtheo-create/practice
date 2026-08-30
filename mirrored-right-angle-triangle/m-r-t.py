# Write a program to make a mirrored right-angled triangle?

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    for j in range(i+1):
        print("*", end='')
    print()

