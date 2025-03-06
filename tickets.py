print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
#height
if height >= 120:
    print("You can ride the rollercoaster")
    #age
    age = int(input("What is your age? "))
    if age >= 10 and age < 18:
        print("Please pay R10.")
        bill += 10
    elif age >= 18 and age < 45:
        print("Please pay R20.")
        bill += 20
    elif age >= 45 and age <=55:
        print("You can have a free ride!!Yayy!")
    else:
        print("Please pay R12.")
        bill += 12
    #photos
    photo = input("Do you want to get a picture? Type 'yes' or 'no': ")
    if photo == "yes":
        print("Photos are R5")
        bill += 5
    else:
        print("Okay.")
else:
    print("Sorry you have to grow taller before you can ride.")

print(f"Your total bill is: R{bill}")