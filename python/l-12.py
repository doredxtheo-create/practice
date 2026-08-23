

# Diamod Star Pattern 1,3,5,7,5,3,1
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# Top Half of the Diamond

# n=4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end='')
#     for j in range(2*i+1):
#         print("*", end='')
#     print()

# # Bottom Half of the Diamond

# for i in range(n-2, -1, -1):
#     for j in range(n-i-1):
#         print(" ", end='')
#     for j in range(2*i+1):
#         print("*", end='')
#     print()

# summarize into a function

def print_diamond(n):
    # Top Half of the Diamond
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end='')
        for j in range(2*i+1):
            print("*", end='')
        print()

    # Bottom Half of the Diamond
    for i in range(n-2, -1, -1):
        for j in range(n-i-1):
            print(" ", end='')
        for j in range(2*i+1):
            print("*", end='')
        print()

print_diamond(4)

