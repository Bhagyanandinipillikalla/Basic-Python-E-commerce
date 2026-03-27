# ------------------ CONSTANTS ------------------
STORE_NAME="Python Store"
CURRENCY="Rs."

# ------------------ DATA ------------------
products = {
    "101":{"name":"Headphones","price":500},
    "102":{"name":"Laptop","price":45000},
    "103":{"name":"Smart Watch","price":2500}
}

cart = {}

# ------------------ FUNCTIONS ------------------
def show_products():
    print("\n--- Available Products ---")
    for pid, item in products.items():
        print(f"ID: {pid} | {item['name']} | {CURRENCY}.{item['price']}")

def add_cart():
    pid = input("Enter Product ID: ")

    if pid not in products:
        print("❌ Product not found!")
        return

    try:
        qty = int(input("Enter Quantity: "))
        if qty <= 0:
            print("Quantity must be greater than 0")
            return
    except ValueError:
        print("❌ Enter a valid number")
        return

    if pid in cart:
        cart[pid]['qty'] += qty
    else:
        cart[pid] = {
            "name": products[pid]['name'],
            "price": products[pid]['price'],
            "qty": qty
        }

    print("✅ Item added to cart")

def view_bill():
    if not cart:
        print("🛒 Cart is empty")
        return

    total = 0
    print("\n--- YOUR BILL ---")
    for item in cart.values():
        cost = item['price'] * item['qty']
        print(f"{item['name']} x {item['qty']} = {CURRENCY}.{cost}")
        total += cost

    print("-" * 30)
    print(f"Total Amount: {CURRENCY}.{total}")

# ------------------ MAIN PROGRAM ------------------
print(f"--- Welcome to {STORE_NAME} ---")

while True:
    print("\n1. View Products")
    print("2. Add to Cart")
    print("3. View Bill & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_cart()

    elif choice == "3":
        view_bill()
        print("🙏 Thank you for shopping!")
        break

    else:
        print("❌ Invalid choice, try again")
