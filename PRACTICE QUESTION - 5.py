# You are analyzing sales data of an online store.
# Use NumPy to generate:
# 1000 random product prices (100 to 1000)
# 1000 random quantities sold (1 to 10)
# Create a Pandas DataFrame with:
# "Price"
# "Quantity"
# Create a new column:
# "Revenue" = Price × Quantity
# Create another column "Category":
# Revenue ≥ 5000 → "High"
# Revenue 2000–4999 → "Medium"
# Revenue < 2000 → "Low"
# Find:
# Total revenue per category
# Average quantity per category
# Top 5 highest revenue transactions
# Visualization:
# Seaborn: Box plot of Revenue by Category
# Matplotlib: Scatter plot of Price vs Revenue

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

prices = np.random.randint(100, 1001, 1000)
quantities = np.random.randint(1, 11, 1000)

df = pd.DataFrame({
    "Price": prices,
    "Quantity": quantities
})

df["Revenue"] = df["Price"] * df["Quantity"]

# Step 4: Categorization
def categorize(rev):
    if rev >= 5000:
        return "High"
    elif rev >= 2000:
        return "Medium"
    else:
        return "Low"

df["Category"] = df["Revenue"].apply(categorize)

total_revenue = df.groupby("Category")["Revenue"].sum()
avg_quantity = df.groupby("Category")["Quantity"].mean()
top5 = df.nlargest(5, "Revenue")

print("Total Revenue:\n", total_revenue)
print("\nAverage Quantity:\n", avg_quantity)
print("\nTop 5 Transactions:\n", top5)

sns.boxplot(x="Category", y="Revenue", data=df)
plt.title("Revenue Distribution by Category")
plt.show()

plt.scatter(df["Price"], df["Revenue"])
plt.title("Price vs Revenue")
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.show()
