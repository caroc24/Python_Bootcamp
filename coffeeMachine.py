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
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}mg\nMoney: ${money}"

def coffee_machine():
    machine_is_on: True
    while machine_is_on:
        coffee_order = input("What would you like? (espresso/latte/cappuccino)")
        if coffee_order == 'report':
            print()
        if coffee_order == 'off':
            machine_is_on = False

coffee_machine()