# Operator.py ( Imaginary name btw)


# List Operators

operators = ['+', '-', '*', '/', '%', '**', '//']

print("\nList of Operators: ", operators)


print(2**6)


# Est-1

amount = int(input("Enter The Amount For Withdrawl jk: "))

note_1 = amount // 100

note_2 = ( amount % 100 ) // 50 

note_3 = ((amount % 100) % 50)

print("Notes Of 100 Bucks:", note_1)
print("Notes of 50 Bucks:", note_2)
print("Notes of 10 Bucks:", note_3)


# Assignment 2:

print("Enter The Marks Obtained In Four Subjects")

math = 40

hindi = 28

english = 80

total = (math+hindi+english)

percentage = ( total / 300 ) * 100

print("The Total Marks Are: ",total)

print("The Percebtage Of The STident Are: ",percentage)

avrage = ( total / 3 )

print(avrage)

if avrage == total:
    print("True")
else:
    print("False")