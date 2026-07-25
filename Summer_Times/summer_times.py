
# Rohan is bored wearing the jacket and pullover now. He wants to wear something light and soft. But he also doesn't want to get the cold by not wearing weather-appropriate clothes. So he will design a program and check what temperature is suitable for wearing light clothes.

temp = int(input("Enter today's temperature: "))

if temp > 25:
    print("It's warm! Wear light clothes like a t-shirt.")
    outfit = "t-shirt"
elif temp > 15:
    print("It's mildly cool. A light jacket would be nice.")
    outfit = "light jacket"
elif temp > 5:
    print("It's cold. Wear a pullover.")
    outfit = "pullover"
else:
    print("It's freezing! Wear a heavy jacket.")
    outfit = "heavy jacket"

print("Recommended outfit:", outfit)
