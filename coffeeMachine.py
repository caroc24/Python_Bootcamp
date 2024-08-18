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


def coffee_machine():
    machine_is_on = True
    while machine_is_on:
        coffee_order = input("What would you like? (espresso/latte/cappuccino) ")
        if coffee_order == 'off':
            machine_is_on = False
        elif coffee_order == 'report':
            report()
        else:
            coffee_order == 'espresso'
            if check_resources(coffee_order):
                espresso_cost = MENU[coffee_order]['ingredients']['cost']
                money_inserted = process_coins()
                if money_inserted > espresso_cost:
                    change = money_inserted - espresso_cost
                    resources["money"].append(1.50)
                    print(f"Here is {change} dollars in change.")


coffee_machine()