# Define menu of resturant
menu = {
    'Veg momo': 110,'Chicken momo': 120,'Buff momo': 130,
    'Veg pizza': 140,'Chicken pizza': 280,'Mix pizza': 320,
    'Americano': 110,'Cappuccino': 210,'Latte': 230,'Mocha': 250,


}
print ("Welcome to Bhaichung Restro.")
print ("Coffee \n Americano: 110, Cappuccino: 210, Latte: 230, Mochha: 250 \nMomo \n Veg momo: 110, Chicken momo: 120, Buff momo: 130 \nPizza \n Veg pizza: 140, Chicken pizza: 280, Mix pizza: 320 ")

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
        order_total += menu[iteam2]
        print(f"{iteam2} is added in your order.")
    else:
        print(f"{iteam2} is not aviable in Bhaichung Restro.")
print(f"Total bill = {order_total}")