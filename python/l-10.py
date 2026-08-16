for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even")

# Assignment:1

string_input = input("Enter Your Word: ")
character = input("Enter Your Character: ")
i  = 0
count = 0
while i < len(string_input):
    if string_input[i] == character:
        count += 1
    i += 1
print(f"The character '{character}' appears {count} times in the word '{string_input}'.")


