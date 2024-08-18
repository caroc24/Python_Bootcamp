MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    global profit
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}mg\nMoney: ${profit}")


def check_resources(drink):
    """Returns true when order can be made, and false when it can't."""
    req_water = MENU[drink]['ingredients']['water']
    req_milk = MENU[drink]['ingredients']['milk']
    req_coffee = water = MENU[drink]['ingredients']['coffee']

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    if water < req_water:
        print("Sorry there is not enough water.")
        return False
    elif milk < req_milk:
        print("Sorry there is not enough milk.")
        return False
    elif coffee < req_coffee:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.\n")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total_money = quarters + dimes + nickels + pennies
    return total_money


def is_transaction_successful(money_received, drink_cost):
    """Returns true if payment is enough. Returns false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def coffee_machine():
    machine_is_on = True
    while machine_is_on:
        coffee_order = input("What would you like? (espresso/latte/cappuccino) ")
        if coffee_order == 'off':
            machine_is_on = False
        elif coffee_order == 'report':
            report()
        else:
            coffee_order = MENU[coffee_order]
            if check_resources(coffee_order):
                money_inserted = process_coins()


coffee_machine()