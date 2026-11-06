import json
from pathlib import Path

PRODUCT_FILE = Path(__file__).with_name("products.json")
cart = []


def load_products():
    """Load products from the JSON file, creating an empty list if needed."""
    if not PRODUCT_FILE.exists():
        return []

    try:
        with PRODUCT_FILE.open("r", encoding="utf-8") as file:
            products = json.load(file)
            return products if isinstance(products, list) else []
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load products: {error}")
        return []


def save_products(products):
    """Save products to the JSON file."""
    try:
        with PRODUCT_FILE.open("w", encoding="utf-8") as file:
            json.dump(products, file, indent=4)
    except OSError as error:
        print(f"Could not save products: {error}")


def display_products(products):
    print("\nAVAILABLE PRODUCTS")
    print("-" * 50)

    if not products:
        print("No products available yet.")
        return

    for product in products:
        print(
            f"ID: {product['id']} | "
            f"{product['name']} | "
            f"₹{product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )


def add_to_cart(products):
    try:
        product_id = int(input("Enter Product ID: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    for product in products:
        if product["id"] == product_id:
            if product["stock"] <= 0:
                print("Sorry, this product is out of stock.")
                return

            # Save a copy so cart entries don't change when product stock changes.
            cart.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
            })

            product["stock"] -= 1
            save_products(products)
            print(f"{product['name']} added to cart.")
            return

    print("Product not found.")


def view_cart():
    print("\nYOUR CART")
    print("-" * 50)

    if not cart:
        print("Cart is empty.")
        return

    total = 0

    for item in cart:
        print(f"{item['name']} — ₹{item['price']:.2f}")
        total += item["price"]

    print("-" * 50)
    print(f"TOTAL = ₹{total:.2f}")


def admin_add_product(products):
    name = input("Product Name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock: ").strip())
    except ValueError:
        print("Enter a valid price and a whole number for stock.")
        return

    if price < 0 or stock < 0:
        print("Price and stock cannot be negative.")
        return

    next_id = max((product["id"] for product in products), default=0) + 1

    products.append({
        "id": next_id,
        "name": name,
        "price": price,
        "stock": stock,
    })

    save_products(products)
    print(f"Product added successfully with ID {next_id}.")


def checkout(products):
    if not cart:
        print("Cart is empty.")
        return

    total = sum(item["price"] for item in cart)

    print("\nCHECKOUT")
    print("-" * 30)
    print(f"Amount to pay: ₹{total:.2f}")
    print("Order placed successfully.")

    cart.clear()


def menu():
    products = load_products()

    while True:
        print("\n===== E-COMMERCE SYSTEM =====")
        print("1. View Products")
        print("2. Add To Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Admin Add Product")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            display_products(products)
        elif choice == "2":
            add_to_cart(products)
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout(products)
        elif choice == "5":
            admin_add_product(products)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    menu()
