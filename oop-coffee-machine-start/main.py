from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine = CoffeeMaker()
my_money = MoneyMachine()
my_menu = Menu()

# espresso = MenuItem("espresso", 50, 0, 18, 1.5)
# latte = MenuItem("latte", 200, 150, 24, 2.5)
# cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

is_on = True

while is_on:
    print(f"This is our current menu: {my_menu.get_items()}")
    order = input("What would you like? ")

    if order == "off":
        is_on = False
    elif order == "report":
        my_machine.report()
        my_money.report()
    else:
        drink = my_menu.find_drink(order)
        if my_machine.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
            my_machine.make_coffee(drink)