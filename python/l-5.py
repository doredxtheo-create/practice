# assigment 1 -> this is inevitability

a = "a"
b = a

if a == b:
    print("a = b")

rain = True

if rain == True:
    print("take an umbrella")

# assignmemt 2 ->

temp_input = int(input("enter todays temprature: "))

if temp_input < 20:
    outfit = "jacket"
    print("it is very cold today....")
    print("wear a ", outfit, " today")
else:
    outfit = "t-shirt"
    print("it is normally warm today")
    print("wear a "+outfit+" today")

# assigment 3 ->

check_rain = input("is it raining today? (yes/no) ")
if check_rain == "yes":
    print("take an umbrella")
else:
    print("leg")
    
input_int = int(input("enter an integer: "))

if input_int % 2 == 0:  # if return = 0 then even else odd -32
    print("the integer is even")
else:
    print("the integer is odd")



num = int(input("enter the integer for correction: "))

if num > 0: # if num = positive print noice else not noice
    print("noice :)")
else:
    print("not noice :( ")

# aight bet


ask_cp = int(input("Enter The Price From Which You have bought it from the store ( i dont care where you got it from ): "))

ask_sp = int(input("How much did you sell it for? "))

# Differeciation

if ask_cp > ask_sp:
    print("Then Learn how to do buissness you had a loss ")
else:
    profit = ask_sp - ask_cp
    print("Im Happy That You Did Something Correct For Once. You Gained A profit of: ",profit)

