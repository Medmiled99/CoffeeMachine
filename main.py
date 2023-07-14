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
}



def resouces_check (order_ingredients):
    """Checks if the resources are sufficient to make the order"""
    for item in order_ingredients:
        if order_ingredients[item] > resources [item]:
            print(f"sorry there is not enough {item}")
            return False
    return True



def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins ")
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes : "))
    nickels = int(input("How many nickels : "))
    pennies = int(input("How many pennies : "))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    print (f"Your Balance is ${total}")
    return total

def money (total , price):


    """checks if money is enough and calculates change"""

    if total < price:
        print ("Sorry, not enough money !")

    elif total == price :
        print("Thank you for your order !")

    elif total > price :
        change = total - price
        print(f"Thank you for your order ! your change is : ${change}")





asba = True
def make_coffee ():
    asba = True
    while asba == True :
        choice = input("What would you like ?: (espresso, latte, or Capuccino)")
        if choice == "report":
            for item in resources:
                print (f" {item} : {resources [item]}")
        

        elif choice == "off":
            asba = False

        item = MENU [choice]
        price = item ["cost"]
        reqs = item ["ingredients"]

        resouces_check(reqs)
        if resouces_check(reqs) == False:
            asba == False
        else:
            total = process_coins()
            money(total, price)
            print(f"here is your {choice}")
            for i in resources:
                resources [i] -= reqs [i]



make_coffee()












