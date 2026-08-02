# Assignment - 1

dashboard_projects = "Visual Studio Code"

vibe_projects = "neovim"


# Moving on..


# Take Input zfor Stude4nt That He can attend The Exam Or Not

medical_cause = input("Do you have any medical cause to attend the exam? (yes/no): "
).strip().lower()

if medical_cause == "yes":
    print("You are allowed to attend the exam.")
else:
    print("You are not allowed to attend the exam.")


# Assignment - 2

# Check if homework_done == true and uniform == true; if hw == true and uniform == false print("You are not allowed to attend the exam. Please wear your uniform.") and if hw == false and uniform == true print("You are not allowed to attend the exam. Please complete your homework.") and if both are false print("You are not allowed to attend the exam. Please complete your homework and wear your uniform."); Nested if/elses are requierd


homework_done = input("Have You Done Your Homewwork? (True/False): ").strip()

uniform = input("Do you have your uniform? (True/False): ").strip()

if homework_done == "True":
    if uniform == "True":
        print("You can Enter ZThe Class.")
    else:
        print("Please wear your uniform.")
else:
    print("Please complete Your HomeWork")