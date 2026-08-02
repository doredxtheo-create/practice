# Raj is a class teacher of grade 10. He wants to design a program that only allows students aged 10 to 20 years in his class. As a result, students whose age is more than 20 can not enroll in his class.

age = int(input("Enter your age: "))
if age >= 10:
    if age <= 20:
        print("You are enrolled.")
    else:
        print("You are not enrolled as your age is greater than 20.")
else:
    print("You are not enrolled as your age is less than 10.")


print("CHECKMATE")

