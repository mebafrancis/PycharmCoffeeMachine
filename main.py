# TODO 2: Check resources sufficient to make drink ordered

MENU={
    "espresso":{
        "ingredients":
            {
                "water": 50,
                "coffee": 18,
                "milk": 0,
            }
    },
    "latte":{
        "ingredients":
            {
                "water": 200,
                "coffee": 24,
                "milk": 150,
            }
    },
    "cappuccino":{
        "ingredients":
            {
                "water": 250,
                "coffee": 24,
                "milk": 100,
            }
    }
}

resources={
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# TODO 1: Print report of all coffee machine resources
is_on= True
profit= 0
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on= False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resources["water"] >= drink["ingredients"]["water"] and resources["milk"] >= drink["ingredients"]["milk"] and resources["coffee"] >= drink["ingredients"]["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            total = quarters + dimes + nickels + pennies
            if total >= 2.5:
                change = round(total - 2.5, 2)
                print(f"Here is ${change} in change.")
                profit += 2.5
                resources["water"] -= drink["ingredients"]["water"]
                resources["milk"] -= drink["ingredients"]["milk"]
                resources["coffee"] -= drink["ingredients"]["coffee"]
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")