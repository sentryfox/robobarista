# robot barista greeting

print("Hello, welcome to Boolean Café!")

name = input("What is your name?\n")

# barista asking about your life choices

life_choice = input("Be honest, " + name + "...Is your bank account okay with this purchase? (Yes or No)\n")
if life_choice != "Yes":
    print("Yeah, in this economy? Save your money. Come back when you're rich!")
    exit()
else:
    print("You're livin' the dream!\n\n\n")

# Coffee menu
# Option must be one listed, otherwise it loops

menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"

while True:
    order = input(name + ", what would you like to order? Here's what we have on our menu.\n" + menu + "\n")

# pricing for beverages

    if order == "Frappuccino":
        price = 6
        break
    elif order == "Black Coffee":
        price = 3
        break
    elif order == "Espresso":
        price = 2
        break
    elif order == "Latte":
        price = 5
        break
    elif order == "Cappuccino":
        price = 4
        break
    else:
        print("Sorry, we don't have that here.")

quantity = input("How many " + order + " " "would you like?\n")

total = price * int(quantity)
print("You got it. Your total is: $" + str(total))

print("Thank you, " + name + ", I'll have your " + quantity + " " + order + " ready for you in a moment.")