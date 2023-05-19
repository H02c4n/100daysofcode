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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = input("How many quarters?: ") * 0.25
    total += input("How many quarters?: ") * 0.1
    total += input("How many quarters?: ") * 0.05
    total += input("How many quarters?: ") * 0.01
    return total


def is_transaction_successful(money_received, drink_coast):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_coast:
        change = round(money_received - drink_coast, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_coast
        return True
    else:
        print("Sorry, that is not enough money. Money refunded")
        return False


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])