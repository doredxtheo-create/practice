
# Radhika wants to design a program in which she can check that the character entered by the user is an alphabet or not.

char = input("Enter a character: ")

if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
    print(char, "is an alphabet.")
else:
    print(char, "is not an alphabet.")



print("CHECKMATE!")