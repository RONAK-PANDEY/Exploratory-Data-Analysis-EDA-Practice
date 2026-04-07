# User Retention & Revenue Analysis
# You are analyzing a platform like Amazon / Flipkart.
# Dataset 1: Transactions (generate with NumPy)
# Create 2000 rows:
# "User_ID" → random (1–200)
# "Date" → random dates within 1 year
# "Amount" → random (100–5000)
# Add:
# Some missing Amount values
# Some duplicate rows
# Dataset 2: Users
# "User_ID" → 1–200
# "Join_Date" → random past dates
# "Region" → "North", "South", "East", "West"
# Tasks
# 1. Data Cleaning
# Remove duplicates
# Fill missing Amount using median per user (tricky)
# 2. Merge
# Combine transactions + users
# 3. Feature Engineering
# Create:
# "Days_Since_Join" = Transaction Date - Join Date
# "Month" from Date
# "User_Lifetime_Value (LTV)" = total spend per user
# 4.Advanced Logic (FAANG Level)
# 🔹 A. Retention Problem
# Find:
# Users who made more than 1 purchase in different months
# (Real retention definition)
# B. Top Users Per Region
# Find top 2 users per region by LTV
# (Window function logic)
# C. Churn Risk Users
# Find users who:
# Have not purchased in the last 90 days
# But had LTV > 10000
# D. Edge Case Logic
# Find:
# Users whose first purchase amount > average purchase of that user
# (VERY tricky — think carefully)
# 5. Visualization
# Seaborn
# Boxplot: LTV by Region
# Matplotlib
# Line plot: Monthly total revenue

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

dates = pd.date_range("2024-01-01", periods=365)

transactions = pd.DataFrame({
    "User_ID": np.random.randint(1, 201, 2000),
    "Date": np.random.choice(dates, 2000),
    "Amount": np.random.randint(100, 5001, 2000).astype(float)
})

transactions.loc[np.random.choice(transactions.index, 50), "Amount"] = np.nan

transactions = pd.concat([transactions, transactions.iloc[:50]])

users = pd.DataFrame({
    "User_ID": np.arange(1, 201),
    "Join_Date": np.random.choice(dates, 200),
    "Region": np.random.choice(["North", "South", "East", "West"], 200)
})

transactions = transactions.drop_duplicates()

transactions["Amount"] = transactions.groupby("User_ID")["Amount"]\
    .transform(lambda x: x.fillna(x.median()))

df = pd.merge(transactions, users, on="User_ID")

df["Days_Since_Join"] = (df["Date"] - df["Join_Date"]).dt.days
df["Month"] = df["Date"].dt.to_period("M")

df["LTV"] = df.groupby("User_ID")["Amount"].transform("sum")

user_months = df.groupby("User_ID")["Month"].nunique()
retained_users = user_months[user_months > 1]

df["Rank"] = df.groupby("Region")["LTV"]\
    .rank(method="first", ascending=False)

top_users = df[df["Rank"] <= 2]

last_date = df["Date"].max()

last_purchase = df.groupby("User_ID")["Date"].max()

churn_users = last_purchase[
    (last_date - last_purchase > pd.Timedelta(days=90))
    ]

high_value = df.groupby("User_ID")["Amount"].sum()
churn_risk = churn_users.index.intersection(
    high_value[high_value > 10000].index
)

avg_amount = df.groupby("User_ID")["Amount"].transform("mean")

first_purchase = df.sort_values("Date").groupby("User_ID").first()

edge_case_users = first_purchase[
    first_purchase["Amount"] > avg_amount.groupby(df["User_ID"]).first()
]


sns.boxplot(x="Region", y="LTV", data=df)
plt.title("LTV by Region")
plt.show()

monthly_revenue = df.groupby("Month")["Amount"].sum()

plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values)
plt.xticks(rotation=45)
plt.title("Monthly Revenue")
plt.show()
