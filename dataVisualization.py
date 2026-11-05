import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample static data for users and products
users = ['alice', 'bob', 'charlie', 'diana', 'edward']
products = [f'Product_{i}' for i in range(1, 11)]  # Product_1 to Product_10

# Generate random purchase data
np.random.seed(42)  # for reproducibility
records = []
for user in users:
    # Each user buys between 1 to 5 products randomly
    purchased_products = np.random.choice(products, size=np.random.randint(1, 6), replace=False)
    for product in purchased_products:
        quantity = np.random.randint(1, 4)  # Each purchase 1 to 3 items
        records.append({'username': user, 'product': product, 'quantity': quantity})

# Create DataFrame
purchases_df = pd.DataFrame(records)

# Ask user for their username
input_user = input("Enter your username: ").strip().lower()

if input_user not in users:
    print("Username not found. Please register first.")
else:
    # Fetch and display user's purchase info
    user_purchases = purchases_df[purchases_df['username'] == input_user]
    if user_purchases.empty:
        print(f"{input_user} has not purchased any products yet.")
    else:
        print(f"\n{input_user.title()}'s Purchased Products:")
        user_summary = user_purchases.groupby('product')['quantity'].sum().reset_index()
        print(user_summary.to_string(index=False))
    
    # Overall product sales analysis
    overall_sales = purchases_df.groupby('product')['quantity'].sum().reset_index()
    overall_sales = overall_sales.sort_values(by='quantity', ascending=False)

    print("\nOverall Top Selling Products:")
    print(overall_sales.to_string(index=False))

    # Plotting
    plt.figure(figsize=(12,6))
    sns.barplot(data=overall_sales, x='product', y='quantity', palette='viridis')
    plt.title('Total Quantity Sold per Product')
    plt.ylabel('Quantity Sold')
    plt.xlabel('Product')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
