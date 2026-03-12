# This is a practice script for a robot barista.

name = input("What is your name?\n")

print("Hello " + name + ", thank you for coming in today.\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappuccino"

print(name + ", what would you like to order? Here is what we are serving.\n" + menu)

order = input()

price = 6

quantity = input("How many would you like?\n")

total = price * int(quantity)
print("You got it. Your total is: $" + str(total))

print("Thank you, " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")