MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}mg\nMoney: ${money}")


def check_resources(drink):
    req_water = MENU[drink]['ingredients']['water']
    req_milk = MENU[drink]['ingredients']['milk']
    req_coffee = water = MENU[drink]['ingredients']['coffee']

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]

    if water < req_water:
        print("Sorry there is not enough water.")
    elif milk < req_milk:
        print("Sorry there is not enough milk.")
    elif coffee < req_coffee:
        print("Sorry there is not enough coffee.")

def process_coins():
    print("Please insert coins.\n")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total_money

def coffee_machine():
    machine_is_on = True
    while machine_is_on:
        coffee_order = input("What would you like? (espresso/latte/cappuccino) ")
        if coffee_order == 'espresso':
            check_resources(coffee_order)
        elif coffee_order == 'report':
            report()
        elif coffee_order == 'off':
            machine_is_on = False

coffee_machine()