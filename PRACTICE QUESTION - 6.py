#PRACTICE QUESTION - 6
# You are given two datasets of an e-commerce platform:
# Dataset 1: Orders
# Generate using NumPy (1000 rows):
# "Order_ID" → 1 to 1000
# "Customer_ID" → random (1 to 100)
# "Product_ID" → random (1 to 50)
# "Quantity" → random (1 to 5), but include some missing values
#  Dataset 2: Products
# Generate:
# "Product_ID" → 1 to 50
# "Price" → random (100 to 1000), include some missing values
# "Category" → randomly assign: "Electronics", "Clothing", "Home"
# Tasks:
# 1. Data Cleaning
# Fill missing Quantity with median
# Fill missing Price with mean
# 2. Merge Datasets
# Combine Orders + Products using "Product_ID"
# 3. Feature Engineering
# Create "Revenue" = Price × Quantity
# 4. Advanced Logic (LeetCode Style )
# Find:
# Top 3 customers by total revenue
# Category with highest average revenue
# Customers who made only 1 order but spent > 3000
# Detect outliers in Revenue (very high values)
# 5. Visualization
# Seaborn:
# Violin plot of Revenue by Category
# Matplotlib:
# Scatter plot: Quantity vs Revenue

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

orders = pd.DataFrame({
    "Order_ID": np.arange(1, 1001),
    "Customer_ID": np.random.randint(1, 101, 1000),
    "Product_ID": np.random.randint(1, 51, 1000),
    "Quantity": np.random.randint(1, 6, 1000).astype(float)
})

orders.loc[np.random.choice(orders.index, 50), "Quantity"] = np.nan

products = pd.DataFrame({
    "Product_ID": np.arange(1, 51),
    "Price": np.random.randint(100, 1001, 50).astype(float),
    "Category": np.random.choice(["Electronics", "Clothing", "Home"], 50)
})

products.loc[np.random.choice(products.index, 5), "Price"] = np.nan

orders["Quantity"] = orders["Quantity"].fillna(orders["Quantity"].median())
products["Price"] = products["Price"].fillna(products["Price"].mean())

df = pd.merge(orders, products, on="Product_ID")

df["Revenue"] = df["Price"] * df["Quantity"]

top_customers = df.groupby("Customer_ID")["Revenue"].sum().nlargest(3)

category_avg = df.groupby("Category")["Revenue"].mean()

customer_orders = df.groupby("Customer_ID").size()
customer_revenue = df.groupby("Customer_ID")["Revenue"].sum()

special_customers = customer_revenue[
    (customer_orders == 1) & (customer_revenue > 3000)
]

threshold = df["Revenue"].mean() + 2 * df["Revenue"].std()
outliers = df[df["Revenue"] > threshold]

print("Top Customers:\n", top_customers)
print("\nCategory Avg Revenue:\n", category_avg)
print("\nSpecial Customers:\n", special_customers)
print("\nOutliers:\n", outliers.head())

sns.violinplot(x="Category", y="Revenue", data=df)
plt.title("Revenue Distribution by Category")
plt.show()

plt.scatter(df["Quantity"], df["Revenue"])
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.title("Quantity vs Revenue")
plt.show()
