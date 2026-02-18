# Simple Shopping Cart Program

def show_menu():
    print("\n==== Shopping Cart Menu ====")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nYour Cart:")
        total = 0
        for item in cart:
            print(f"- {item['name']} : ${item['price']}")
            total += item['price']
        print(f"Total: ${total}")

def main():
    cart = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            cart.append({"name": name, "price": price})
            print(f"{name} added to cart.")

        elif choice == "2":
            name = input("Enter item name to remove: ")
            found = False
            for item in cart:
                if item["name"] == name:
                    cart.remove(item)
                    print(f"{name} removed from cart.")
                    found = True
                    break
            if not found:
                print("Item not found in cart.")

        elif choice == "3":
            view_cart(cart)

        elif choice == "4":
            view_cart(cart)
            print("Thank you for shopping!")
            break

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
