menu = {"pizza"   :   3.00,
        "nachos"  :  4.00,
        "chicken" : 5.00,
        "burger"  :  6.00,
        "lemonade": 7.00,
        "chips"   :   8.00,
        "donuts"  :   9.00,
        "jus"     :      10.00,
        "meat"    :     23.00,
        "fish"    :  28.00 }
print("---------MENU---------")
cart = []
total = 0
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("-------------------------")
while True:
    food =  input("select an items(select q for quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-------YOUR ORDER--------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"total is : ${total:.2f}")
