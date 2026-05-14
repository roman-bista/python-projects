# define the menu options
menu={
    "pizza":40,
    "burger":30,
    "pasta":50,
    "salad":20,
     "coffee":22
}
print("Welcome to our restaurant! Here is our menu:")
print("pizza: $40\n burger: $30\n pasta: $50\n salad: $20\n coffee: $22")

order_total=0

item1=input("Please enter the first item you would like to order: ")
if item1 in menu:
    order_total+=menu[item1]
    print(f"{item1} added to your order. Current total: ${order_total}")
else:
    print(f"Sorry, {item1} is not on the menu.")

another_item=input("Would you like to order another item? (yes/no) ")
if another_item.lower()=="yes":
    item2=input("Please enter the second item you would like to order: ")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"{item2} added to your order. Current total: ${order_total}")
    else:
        print(f"Sorry, {item2} is not on the menu.")
        
print(f"Your final order total is: ${order_total}. Thank you for dining with us!")