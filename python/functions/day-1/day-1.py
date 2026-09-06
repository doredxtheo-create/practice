def total_calc(bill_amount, tip_percentage):
    """
    Calculate the total amount including tip.

    Parameters:
    bill_amount (float): The original bill amount.
    tip_percentage (float): The tip percentage to be added to the bill.

    Returns:
    float: The total amount including tip.
    """
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return total_amount
print(total_calc(200, 12))

# Assignment: 2 ; NOTE: The following function calculates the cube of a number, """" is consodered as a docstring and is used to describe the function's purpose and behavior. It provides information about the function's parameters, return value, and any other relevant details. In this case, the docstring explains that the function calculates the cube of a number.

def cube(number):
    """
    Calculate the cube of a number.

    Parameters:
    number (float): The number to be cubed.

    Returns:
    float: The cube of the input number.
    """
    return number ** 3
print(cube.__doc__)  # Output: Calculate the cube of a number.
print(cube(4))

# Assignment: 3 ; Calculate The Factorial

def fact(g):
    """
    Calculate the factorial of a number.

    Parameters:
    g (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the input number.
    """
    if g == 0 or g == 1:
        return 1
    else:
        return g * fact(g - 1)
print(fact(4))

# Assignment: 4 ; Tasks:

# Create a Python Program using recurrsion to find the sum of numbers from 1 - 5.

def sum(l):
    if l == 0:
        return 0
    else:
        return l + sum(l - 1)

print(sum(5))