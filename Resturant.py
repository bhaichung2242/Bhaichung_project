# Define menu of resturant
menu = {
    'Momo': 120,
    'Pizza': 340,
    'Burger': 220,
    'Sandwich': 140,
}
print ("Welcome to Bhaichung Restro.")
print ("Momo: Rs 120 \nPizza: Rs 340 \nBurger: Rs 220 \nSandwich: Rs 140")

order_total = 0

iteam1 = input("What do you like to order? = ")
if iteam1 in menu:
    order_total += menu[iteam1]
    print(f"{iteam1} has been orderd")
else:
    print(f"{iteam1} is not aviable at our restro.")

another_iteam = input("Do you want to order more? Yes/No = ")
if another_iteam == "Yes":
    iteam2 = input("What do you like to add? = ")
    if iteam2 in menu:
        order_total = menu[iteam2]
        print(f"{iteam2} is added in your order.")
    else:
        print(f"{iteam2} is not aviable in Bhaichung Restro.")
print(f"Total bill = {order_total}")