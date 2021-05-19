#Fast food menu program

foodMenu = [
    #Food item, price, quantity
    ("Chicken Nuggets", 3.50, 0),
    ("Chips", 2.50, 0),
    ("Coca Cola", 1, 0),
    ("Ketchup", 0.5, 0)
    ]

def printIntro():
    print("Welcome to Burger King")
    print()

def printMenu():
    print("Please tell me what you would like to eat:")
    print("1. Chicken Nuggets - £3.50")
    print("2. Chips - £2.50")
    print("3. Coca Cola - £1.00")
    print("4. Ketchup - £0.50")

def askForChoice():
    choice = int(input("Please say which item you would like to get: "))
    quantityOfChoice = int(input("How many of this item would you like to have: "))

print(foodMenu[1])
print(foodMenu[1][1])
