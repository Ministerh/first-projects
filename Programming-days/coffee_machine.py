MENU = {
    "expresso":{
        'ingredient':{
            'water':50,
            'coffee':18
        },
        'cost':1.5

       },
    "latte":{
        'ingredient':{
            'water':200,
            'milk':150,
            'coffee':24
        },
        'cost':2.5
    },
    "cappucino":{
        'ingredient':{
            'water':250,
            'milk':100,
            'coffee':24
        },
        'cost':3.0
    }

}

money = 0
resources = {
    'water':300,
    'milk':200,
    'coffee': 100
}
def coin_processor():
    '''returns total coins calculated'''

    print("please insert coin")
    total = int(input("how many quarters ")) * 0.25
    total += int(input("how many dimes ")) * 0.1
    total += int(input("how many nickles ")) * 0.05
    total += int(input("how many pennies ")) * 0.01
    return total

def successful_transaction(money_rec, drink_cost):
    '''return True if payment is succesful or returns False if coin is not enough'''
    if money_rec > drink_cost:
        change = round(money_rec - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("sorry that's enough money. Money refunded")



def sufficient_resources(flavor):
    '''returns True when orders can be made'''
    for ing in flavor:
        if flavor[ing] >= resources[ing]:
            print(f"Sorry there's not enough {ing}")
            return False
    return True

def make_coffee(flavor, ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"here is your {flavor} ")
    

machine_running = True

while machine_running:
    choice = input("What would you like to take ? (expresso/latte/cappucino):").lower()
    if choice == 'off':
        machine_running = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"coffe: {resources['coffee']}g")
        print(f"Money: ${money}")       
    else:
        drink = MENU[choice]
        if sufficient_resources (drink['ingredient']):
            payment = coin_processor()
            if successful_transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredient'])
               

