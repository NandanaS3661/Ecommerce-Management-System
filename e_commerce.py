
import uuid
from datetime import datetime

# ==========================================
# SAMPLE E-COMMERCE MANAGEMENT SYSTEM
# ==========================================

customer = {
    "name": "Nandana",
    "email": "customer@example.com",
    "phone": "9876543210"
}

# 30 Sample Products
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "rating": 4.5, "stock": 10, "brand": "HP"},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 25000, "rating": 4.6, "stock": 15, "brand": "Samsung"},
    {"id": 3, "name": "Headphones", "category": "Electronics", "price": 1999, "rating": 4.2, "stock": 25, "brand": "Boat"},
    {"id": 4, "name": "Smart Watch", "category": "Electronics", "price": 3499, "rating": 4.1, "stock": 12, "brand": "Noise"},
    {"id": 5, "name": "Bluetooth Speaker", "category": "Electronics", "price": 2499, "rating": 4.4, "stock": 18, "brand": "JBL"},
    {"id": 6, "name": "Keyboard", "category": "Electronics", "price": 899, "rating": 4.0, "stock": 30, "brand": "Logitech"},
    {"id": 7, "name": "Mouse", "category": "Electronics", "price": 599, "rating": 4.3, "stock": 40, "brand": "Dell"},
    {"id": 8, "name": "Tablet", "category": "Electronics", "price": 18000, "rating": 4.5, "stock": 8, "brand": "Lenovo"},
    {"id": 9, "name": "Power Bank", "category": "Electronics", "price": 1299, "rating": 4.2, "stock": 20, "brand": "Mi"},
    {"id": 10, "name": "Webcam", "category": "Electronics", "price": 1599, "rating": 4.0, "stock": 14, "brand": "Logitech"},

    {"id": 11, "name": "T-Shirt", "category": "Fashion", "price": 599, "rating": 4.1, "stock": 50, "brand": "Puma"},
    {"id": 12, "name": "Jeans", "category": "Fashion", "price": 1299, "rating": 4.3, "stock": 35, "brand": "Levis"},
    {"id": 13, "name": "Sneakers", "category": "Fashion", "price": 2499, "rating": 4.6, "stock": 20, "brand": "Nike"},
    {"id": 14, "name": "Handbag", "category": "Fashion", "price": 1799, "rating": 4.2, "stock": 15, "brand": "Lavie"},
    {"id": 15, "name": "Sunglasses", "category": "Fashion", "price": 999, "rating": 4.0, "stock": 22, "brand": "Fastrack"},

    {"id": 16, "name": "Novel Book", "category": "Books", "price": 350, "rating": 4.7, "stock": 40, "brand": "Penguin"},
    {"id": 17, "name": "Python Programming", "category": "Books", "price": 650, "rating": 4.8, "stock": 25, "brand": "TechBooks"},
    {"id": 18, "name": "Science Book", "category": "Books", "price": 450, "rating": 4.3, "stock": 30, "brand": "Oxford"},
    {"id": 19, "name": "History Book", "category": "Books", "price": 400, "rating": 4.1, "stock": 18, "brand": "Pearson"},
    {"id": 20, "name": "Motivational Book", "category": "Books", "price": 299, "rating": 4.5, "stock": 32, "brand": "Harper"},

    {"id": 21, "name": "Water Bottle", "category": "Home", "price": 399, "rating": 4.0, "stock": 50, "brand": "Milton"},
    {"id": 22, "name": "Table Lamp", "category": "Home", "price": 899, "rating": 4.2, "stock": 20, "brand": "Philips"},
    {"id": 23, "name": "Bedsheet", "category": "Home", "price": 1199, "rating": 4.4, "stock": 15, "brand": "Bombay Dyeing"},
    {"id": 24, "name": "Wall Clock", "category": "Home", "price": 699, "rating": 4.1, "stock": 25, "brand": "Ajanta"},
    {"id": 25, "name": "Coffee Mug", "category": "Home", "price": 249, "rating": 4.3, "stock": 60, "brand": "Cello"},

    {"id": 26, "name": "Cricket Bat", "category": "Sports", "price": 1599, "rating": 4.5, "stock": 12, "brand": "SG"},
    {"id": 27, "name": "Football", "category": "Sports", "price": 899, "rating": 4.2, "stock": 20, "brand": "Nivia"},
    {"id": 28, "name": "Yoga Mat", "category": "Sports", "price": 799, "rating": 4.4, "stock": 25, "brand": "Boldfit"},
    {"id": 29, "name": "Badminton Racket", "category": "Sports", "price": 1299, "rating": 4.3, "stock": 16, "brand": "Yonex"},
    {"id": 30, "name": "Skipping Rope", "category": "Sports", "price": 299, "rating": 4.0, "stock": 35, "brand": "Decathlon"}
]

# Shopping cart: {product_id: quantity}
cart = {}

# Order history
orders = []


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def get_amount(value):
    return f"Rs. {value:,.2f}"


def display_product(product):
    print("-" * 75)
    print(f"Product ID : {product['id']}")
    print(f"Name       : {product['name']}")
    print(f"Category   : {product['category']}")
    print(f"Brand      : {product['brand']}")
    print(f"Price      : {get_amount(product['price'])}")
    print(f"Rating     : {product['rating']}/5")
    print(f"Stock      : {product['stock']} units")
    print("-" * 75)


def get_valid_id(message):
    try:
        return int(input(message))
    except ValueError:
        print("Please enter a valid number.")
        return None


def get_valid_quantity(message):
    try:
        quantity = int(input(message))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return None
        return quantity
    except ValueError:
        print("Please enter a valid quantity.")
        return None


# ==========================================
# 1. VIEW ALL PRODUCTS
# ==========================================

def view_products():
    print("\n========== ALL PRODUCTS ==========")
    print(f"{'ID':<5}{'PRODUCT':<25}{'CATEGORY':<15}{'PRICE':<15}{'RATING':<10}")
    print("-" * 75)

    for p in products:
        print(
            f"{p['id']:<5}"
            f"{p['name']:<25}"
            f"{p['category']:<15}"
            f"{get_amount(p['price']):<15}"
            f"{p['rating']}/5"
        )

    print("-" * 75)
    print(f"Total Products: {len(products)}")


# ==========================================
# 2. SEARCH PRODUCTS
# ==========================================

def search_products():
    keyword = input("\nEnter product name or brand: ").strip().lower()

    if not keyword:
        print("Search term cannot be empty.")
        return

    results = [
        p for p in products
        if keyword in p["name"].lower()
        or keyword in p["brand"].lower()
    ]

    if results:
        print("\n========== SEARCH RESULTS ==========")
        for p in results:
            display_product(p)
    else:
        print("No matching products found.")


# ==========================================
# 3. FILTER BY CATEGORY
# ==========================================

def filter_category():
    categories = sorted(set(p["category"] for p in products))

    print("\n========== PRODUCT CATEGORIES ==========")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    choice = get_valid_id("Select category number: ")

    if choice is None or not 1 <= choice <= len(categories):
        print("Invalid category selection.")
        return

    selected = categories[choice - 1]

    print(f"\nProducts in {selected}:")
    for p in products:
        if p["category"] == selected:
            display_product(p)


# ==========================================
# 4. PRODUCT DETAILS
# ==========================================

def product_details():
    product_id = get_valid_id("\nEnter Product ID: ")

    if product_id is None:
        return

    product = get_product(product_id)

    if product:
        print("\n========== PRODUCT DETAILS ==========")
        display_product(product)
    else:
        print("Product not found.")


# ==========================================
# 5. ADD TO CART
# ==========================================

def add_to_cart():
    view_products()

    product_id = get_valid_id("\nEnter Product ID to add: ")

    if product_id is None:
        return

    product = get_product(product_id)

    if not product:
        print("Invalid Product ID.")
        return

    quantity = get_valid_quantity("Enter quantity: ")

    if quantity is None:
        return

    current_quantity = cart.get(product_id, 0)

    if current_quantity + quantity > product["stock"]:
        print(f"Only {product['stock'] - current_quantity} more units available.")
        return

    cart[product_id] = current_quantity + quantity

    print(f"\n{product['name']} added to cart successfully!")


# ==========================================
# 6. VIEW CART
# ==========================================

def view_cart():
    print("\n========== YOUR SHOPPING CART ==========")

    if not cart:
        print("Your cart is empty.")
        return

    total = 0

    print(f"{'PRODUCT':<25}{'PRICE':<15}{'QTY':<8}{'SUBTOTAL':<15}")
    print("-" * 65)

    for product_id, quantity in cart.items():
        p = get_product(product_id)
        subtotal = p["price"] * quantity
        total += subtotal

        print(
            f"{p['name']:<25}"
            f"{get_amount(p['price']):<15}"
            f"{quantity:<8}"
            f"{get_amount(subtotal):<15}"
        )

    print("-" * 65)
    print(f"Cart Total: {get_amount(total)}")


# ==========================================
# 7. UPDATE CART QUANTITY
# ==========================================

def update_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    product_id = get_valid_id("\nEnter Product ID to update: ")

    if product_id is None:
        return

    if product_id not in cart:
        print("Product is not in your cart.")
        return

    quantity = get_valid_quantity("Enter new quantity: ")

    if quantity is None:
        return

    product = get_product(product_id)

    if quantity > product["stock"]:
        print(f"Only {product['stock']} units are available.")
        return

    cart[product_id] = quantity
    print("Cart quantity updated successfully!")


# ==========================================
# 8. REMOVE FROM CART
# ==========================================

def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    product_id = get_valid_id("\nEnter Product ID to remove: ")

    if product_id is None:
        return

    if product_id in cart:
        product = get_product(product_id)
        del cart[product_id]
        print(f"{product['name']} removed from cart.")
    else:
        print("Product not found in cart.")


# ==========================================
# 9. CHECKOUT AND BILL GENERATION
# ==========================================

def checkout():
    if not cart:
        print("\nYour cart is empty. Add products before checkout.")
        return

    view_cart()

    confirm = input("\nDo you want to place the order? (yes/no): ").strip().lower()

    if confirm not in ("yes", "y"):
        print("Checkout cancelled.")
        return

    # Verify stock again
    for product_id, quantity in cart.items():
        product = get_product(product_id)

        if quantity > product["stock"]:
            print(f"Insufficient stock for {product['name']}. Order cancelled.")
            return

    subtotal = sum(
        get_product(pid)["price"] * qty
        for pid, qty in cart.items()
    )

    gst = subtotal * 0.05
    grand_total = subtotal + gst

    order_id = "ORD-" + uuid.uuid4().hex[:8].upper()

    # Generate bill
    print("\n" + "=" * 65)
    print("                 E-COMMERCE STORE")
    print("                   ORDER INVOICE")
    print("=" * 65)

    print(f"Order ID   : {order_id}")
    print(f"Date       : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"Customer   : {customer['name']}")
    print(f"Email      : {customer['email']}")
    print("-" * 65)

    print(f"{'PRODUCT':<25}{'PRICE':<15}{'QTY':<8}{'TOTAL':<15}")
    print("-" * 65)

    purchased_items = []

    for product_id, quantity in cart.items():
        p = get_product(product_id)
        amount = p["price"] * quantity

        print(
            f"{p['name']:<25}"
            f"{get_amount(p['price']):<15}"
            f"{quantity:<8}"
            f"{get_amount(amount):<15}"
        )

        purchased_items.append({
            "name": p["name"],
            "price": p["price"],
            "quantity": quantity,
            "total": amount
        })

    print("-" * 65)
    print(f"Subtotal       : {get_amount(subtotal)}")
    print(f"GST (5%)       : {get_amount(gst)}")
    print(f"Grand Total    : {get_amount(grand_total)}")
    print("=" * 65)
    print("             THANK YOU FOR SHOPPING!")
    print("=" * 65)

    # Reduce stock only after successful checkout
    for product_id, quantity in cart.items():
        get_product(product_id)["stock"] -= quantity

    # Save order in history
    orders.append({
        "order_id": order_id,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "items": purchased_items,
        "subtotal": subtotal,
        "gst": gst,
        "total": grand_total
    })

    cart.clear()

    print("\nOrder placed successfully!")


# ==========================================
# 10. ORDER HISTORY
# ==========================================

def order_history():
    print("\n========== ORDER HISTORY ==========")

    if not orders:
        print("No orders have been placed yet.")
        return

    for order in orders:
        print("-" * 60)
        print(f"Order ID : {order['order_id']}")
        print(f"Date     : {order['date']}")

        for item in order["items"]:
            print(
                f"  {item['name']} x {item['quantity']} "
                f"= {get_amount(item['total'])}"
            )

        print(f"Total    : {get_amount(order['total'])}")

    print("-" * 60)
    print(f"Total Orders: {len(orders)}")


# ==========================================
# 11. CUSTOMER PROFILE
# ==========================================

def customer_profile():
    print("\n========== CUSTOMER PROFILE ==========")
    print(f"Name  : {customer['name']}")
    print(f"Email : {customer['email']}")
    print(f"Phone : {customer['phone']}")
    print(f"Orders: {len(orders)}")
    print(f"Cart Items: {sum(cart.values())}")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    print("\n" + "=" * 55)
    print("       WELCOME TO ONLINE SHOPPING SYSTEM")
    print("=" * 55)

    while True:

        print("\n=============== MAIN MENU ===============")
        print("1.  View All Products")
        print("2.  Search Products")
        print("3.  Filter Products by Category")
        print("4.  View Product Details")
        print("5.  Add Product to Cart")
        print("6.  View Shopping Cart")
        print("7.  Update Cart Quantity")
        print("8.  Remove Product from Cart")
        print("9.  Checkout and Generate Bill")
        print("10. View Order History")
        print("11. View Customer Profile")
        print("12. Exit")
        print("=========================================")

        choice = input("Enter your choice (1-12): ").strip()

        if choice == "1":
            view_products()

        elif choice == "2":
            search_products()

        elif choice == "3":
            filter_category()

        elif choice == "4":
            product_details()

        elif choice == "5":
            add_to_cart()

        elif choice == "6":
            view_cart()

        elif choice == "7":
            update_cart()

        elif choice == "8":
            remove_from_cart()

        elif choice == "9":
            checkout()

        elif choice == "10":
            order_history()

        elif choice == "11":
            customer_profile()

        elif choice == "12":
            print("\nThank you for visiting our online store!")
            print("Have a great day!")
            break

        else:
            print("\nInvalid choice! Please select between 1 and 12.")


# ==========================================
# PROGRAM STARTS HERE
# ==========================================

if __name__ == "__main__":
    main()
