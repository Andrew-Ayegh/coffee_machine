from os import system

from art import coffee_machine

def monetary_value():
    '''takes quarters, dimes, nickles & pennies and converts to dollar monetary value '''
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies =int(input("How many pennies?: "))
    value = ((25*quarters)/100 +(10*dimes)/100 + (5*nickles)/100 + (pennies/100) )
    return value


menu= {
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
}

cash = 0

machine_on =True
# coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

while machine_on:
    
    print(coffee_machine)
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if coffee_type == "off":
        machine_on = False
    
    elif coffee_type == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")    
    elif coffee_type == "espresso":
        print("Please insert coin")

        
        money = round(monetary_value(), 2)
        
        print(f"\nyour total money: ${money}")
        
        if money >= menu["espresso"]["cost"]:
            if resources["water"] > menu["espresso"]["ingredients"]["water"]:
                if resources["coffee"] > menu["espresso"]["ingredients"]["coffee"]:
                    cash += menu["espresso"]["cost"]
                    round(cash, 2)
                    resources["water"] -= menu["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
                    change = round((money - menu["espresso"]["cost"]), 2)
                    
                    # print(change)
                    # print(money)
                    # print(cash)
                    print(f"\n\nHere is your {coffee_type}. Enjoy!")
                    if change > 0:
                        print(f"\nhere is your ${change} change")
                else:
                    print("sorry not enough coffee")
            else:
                print("sorry, not enough water")
        else:
            print("Sorry that's not enough money. Money refunded.")
    
    elif coffee_type == "latte":
        print("Please insert coin")
        
        money = round(monetary_value(), 2)
        
        print(f"\nyour total money is: ${money}")
        
        
        if money >= menu["latte"]["cost"]:
            if resources["water"] > menu["latte"]["ingredients"]["water"]:
                if resources["coffee"] > menu["latte"]["ingredients"]["coffee"]:
                    if resources["milk"] > menu["latte"]["ingredients"]["milk"]:
                        
                        cash += menu["latte"]["cost"]
                        resources["water"] -= menu["latte"]["ingredients"]["water"]
                        resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
                        change =round( (money - menu["latte"]["cost"]), 2)
                        
                        # print(change)
                        # print(money)
                        # print(cash)
                        
                        print(f"\n\nHere is your {coffee_type}. Enjoy!")
                        if change > 0:
                            print(f"\nhere is your ${change} change")
                    else:
                        print("sorry not enough milk")
                else:
                    print("sorry, not enough coffee")
            else:
                print("Sorry, not enough water.")
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif coffee_type == "cappuccino":
        print("Please insert coin")
        
        money = round(monetary_value(), 2)
        
        print(f"\nyour total money is: ${money}")
        
        
        if money >= menu["cappuccino"]["cost"]:
            if resources["water"] > menu["cappuccino"]["ingredients"]["water"]:
                if resources["coffee"] > menu["cappuccino"]["ingredients"]["coffee"]:
                    if resources["milk"] > menu["cappuccino"]["ingredients"]["milk"]:
                        
                        cash += menu["cappuccino"]["cost"]
                        resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
                        resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
                        change =round((money - menu["latte"]["cost"]), 2)
                        
                        # print(change)
                        # print(money)
                        # print(cash)
                        print(f"\n\nHere is your {coffee_type}. Enjoy!")
                        if change > 0:
                            print(f"\nhere is your ${change} change")
                    else:
                        print("sorry not enough milk")
                else:
                    print("sorry, not enough coffee")
            else:
                print("Sorry, not enough water.")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("choose your preferable coffee type")
    system('cls')
