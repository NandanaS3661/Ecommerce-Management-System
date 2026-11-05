import json

PRODUCT_FILE = "products.json"
cart = []


def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_products(products):
    with open(PRODUCT_FILE, "w") as file:
        json.dump(products, file, indent=4)


def display_products(products):
    print("\nAVAILABLE PRODUCTS")
    print("-" * 40)

    for product in products:
        print(
            f"ID: {product['id']} | "
            f"{product['name']} | "
            f"₹{product['price']} | "
            f"Stock: {product['stock']}"
        )


def add_to_cart(products):
    try:
        product_id = int(input("Enter Product ID: "))

        for product in products:
            if product["id"] == product_id:

                if product["stock"] > 0:
                    cart.append(product)
                    product["stock"] -= 1

                    save_products(products)

                    print("Item added to cart")
                    return

                else:
                    print("Out of stock")
                    return

        print("Product not found")

    except ValueError:
        print("Invalid input")


def view_cart():
    total = 0

    print("\nYOUR CART")
    print("-" * 40)

    if len(cart) == 0:
        print("Cart is empty")
        return

    for item in cart:
        print(f"{item['name']} - ₹{item['price']}")
        total += item["price"]

    print("-" * 40)
    print(f"TOTAL = ₹{total}")


def admin_add_product(products):
    try:
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        new_product = {
            "id": len(products) + 1,
            "name": name,
            "price": price,
            "stock": stock
        }

        products.append(new_product)

        save_products(products)

        print("Product added successfully")

    except ValueError:
        print("Invalid Input")


def checkout():
    if not cart:
        print("Cart is empty")
        return

    total = sum(item["price"] for item in cart)

    print("\nCHECKOUT")
    print(f"Amount to Pay = ₹{total}")
    print("Order Placed Successfully")

    cart.clear()


def menu():
    products = load_products()

    while True:

        print("\n")
        print("===== E-COMMERCE SYSTEM =====")
        print("1. View Products")
        print("2. Add To Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Admin Add Product")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_products(products)

        elif choice == "2":
            add_to_cart(products)

        elif choice == "3":
            view_cart()

        elif choice == "4":
            checkout()

        elif choice == "5":
            admin_add_product(products)
            products = load_products()

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()