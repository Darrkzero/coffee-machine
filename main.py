MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
}


def coin():
    print("please insert your coin.")
    quarter = float(input("how many quarters "))
    quarter *= 0.25
    dimes = float(input("how many dimes "))
    dimes *= 0.10
    nickles = float(input("how many nickles "))
    nickles *= 0.05
    pennies = float(input("how many pennies "))
    pennies *= 0.01
    total_amount = quarter + dimes + nickles + pennies
    if total_amount < MENU[choice]["cost"]:
        return "sorry that is not enough money. Money refunded"
    elif total_amount > MENU[choice]["cost"]:
        change = total_amount - MENU[choice]["cost"]
        return f"here is ${round(change,2)} in change"


def sufficient_resource(drink):
    if resources["water"] > drink["water"] and resources["milk"] > drink["milk"] and resources["coffee"] > drink["coffee"]:
        water = resources["water"] - drink["water"]
        milk = resources["milk"] - drink["milk"]
        coffee = resources["coffee"] - drink["coffee"]
        resources["water"] = water
        resources["milk"] = milk
        resources["coffee"] = coffee
        return f"Here is your {choice} ☕☕. Enjoy!"
    elif resources["water"] < drink["water"]:
        return f"There is not enough water."
    elif resources["milk"] < drink["milk"]:
        return f"There is not enough milk."
    elif resources["coffee"] < drink["coffee"]:
        return f"there is not enough coffee"


def resource():

    return f"water : {resources['water']}\nmilk : {resources['milk']}\ncoffee : { resources['coffee']}"


def espresso():
    return sufficient_resource(MENU["espresso"]["ingredients"])


def latte():
    return sufficient_resource(MENU["latte"]["ingredients"])


def cappuccino():
    return sufficient_resource(MENU["cappuccino"]["ingredients"])


proceed = True
while proceed:
    choice = input("what would you like? (espresso/latte/cappuccino) ")
    if choice == "report":
        print(resource())
    elif choice == "latte":
        print(coin())
        print(latte())
    elif choice == "espresso":
        print(coin())
        print(espresso())
    elif choice == "cappuccino":
        print(coin())
        print(cappuccino())
    elif choice == "off":
        proceed = False
