# Day 4 Bonus Challenge 2: Shopping Cart

print("=== Shopping Cart ===")
print()

# Available items
items = {
    "1": {"name": "Apple", "price": 0.99},
    "2": {"name": "Bread", "price": 2.50},
    "3": {"name": "Milk", "price": 3.99},
    "4": {"name": "Eggs", "price": 4.50}
}

cart = []  # Store purchased items
total = 0

while True:
    # Display menu
    print("\n=== Available Items ===")
    # Your code: loop through items and display
    for key,item in items.items():
        print(f"{key}.{item['name']}-{item['price']}")
    print("5.Checkout")
    
    choice = input("\nSelect item (1-5): ")
    
    # Your code:
    # If choice is 1-4: add to cart, update total
    # If choice is 5: break and show receipt
    # Handle invalid input
    if choice in ["1","2","3","4"]:
        cart.append(items[choice]["name"])
        total+=items[choice]["price"]
        print(f"✅ Added {items[choice]['name']} to cart!")
    elif choice=="5":
        if len(cart)==0:
            print("your cart is empty")
        else:
            break
    else:
        print("❌ Invalid choice. Please select 1-5.")

    
# After loop, show receipt
print("\n=== Your Receipt ===")
for item in cart:
    print(f"- {item}")
print(f"\nTotal: ${total:.2f}")
print("\nThank you for shopping! 🛒")