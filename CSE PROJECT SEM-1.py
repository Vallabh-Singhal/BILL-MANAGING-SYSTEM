def print_bill():
    menu = {
        1: {"item": "Pizza", "price": 120.00},
        2: {"item": "Pasta", "price": 150.00},
        3: {"item": "Burger", "price": 80.00},
        4: {"item": "Biscoff Shake", "price": 200.00},
        5: {"item": "Soup", "price": 110.00},
        6: {"item": "Fries", "price": 100.00},
        7: {"item": "Coke", "price": 70.00},
        8: {"item": "Juice", "price": 90.00},
        9: {"item": "Coffee", "price": 80.00},
        10: {"item": "Brownie", "price": 150.00}
    }

    order = {}
    total_bill = 0.0

    print("--- Our Menu ---")
    for item_id, details in menu.items():
        print(f"{item_id}. {details['item']} - Rs {details['price']}")
    print("----------------")
    while True:
        choice = input("Enter item number to order (or 'done' to finish): ").lower()
        if choice == 'done':
            break
        item_id = int(choice)
        if item_id in menu:
            qty = int(input(f"Enter quantity for {menu[item_id]['item']}: "))
            if qty > 0:
                order[item_id] = order.get(item_id,0) + qty
            else:
                print("Quantity of ordered item can't be 0.")
        else:
            print("Invalid item number. Please choose from the menu.")

    print("\n--- Your Bill ---")
    print(f"{'Item:'}     {'Quantity'}     {'Price'}     {'Subtotal'}")
    print("-" * 50)

    for item_id, qty in order.items():
        item_name = menu[item_id]['item']
        item_price = menu[item_id]['price']
        subtotal = item_price * qty
        total_bill += subtotal
        print(f"{item_name:<11}     {qty}     Rs {item_price:}     Rs {subtotal:}")

    print("-" * 50)
    print(f"{'Total: '}Rs {total_bill:}")
    print("-----------------")

print_bill()