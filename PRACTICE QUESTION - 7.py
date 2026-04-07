# Time-Series Sales Analysis
# You are given daily sales data of an online platform for 2 years (730 days).
# Tasks
# 1. Data Generation (NumPy)
# Create dataset with:
# "Date" → daily dates
# "Sales" → random (1000 to 10000)
# "Customers" → random (50 to 500)
# Add:
# Some missing values in Sales
# Some extreme spikes (outliers)
# 2. Data Cleaning
# Fill missing Sales using forward fill
# Handle outliers using clipping (limit values)
# 3. Feature Engineering
# Create:
# "Revenue_per_Customer" = Sales / Customers
# "7_day_MA" → 7-day moving average of Sales
# "Growth" → % change in Sales
# 4. Advanced Logic (Interview Level)
# Find:
# Top 5 days with highest growth spike
# Longest streak of increasing sales days
# Days where:
# Sales > 7-day average
# AND Growth > 10%
# 5. Visualization
# Seaborn:
# Lineplot of Sales + Moving Average
# Matplotlib:
# Highlight spike days on graph

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", periods=730)

df = pd.DataFrame({
    "Date": dates,
    "Sales": np.random.randint(1000, 10000, 730).astype(float),
    "Customers": np.random.randint(50, 500, 730)
})

df.loc[np.random.choice(df.index, 20), "Sales"] = np.nan

df.loc[np.random.choice(df.index, 10), "Sales"] *= 5

df["Sales"] = df["Sales"].ffill()

upper_limit = df["Sales"].quantile(0.99)
df["Sales"] = df["Sales"].clip(upper=upper_limit)

df["Revenue_per_Customer"] = df["Sales"] / df["Customers"]

df["7_day_MA"] = df["Sales"].rolling(window=7).mean()

df["Growth"] = df["Sales"].pct_change() * 100


top_growth = df.nlargest(5, "Growth")

streak = (df["Sales"].diff() > 0).astype(int)
df["streak_group"] = (streak == 0).cumsum()
longest_streak = streak.groupby(df["streak_group"]).sum().max()

special_days = df[
    (df["Sales"] > df["7_day_MA"]) &
    (df["Growth"] > 10)
]

print("Top Growth Days:\n", top_growth[["Date", "Growth"]])
print("\nLongest Increasing Streak:", longest_streak)
print("\nSpecial Days:\n", special_days.head())

sns.lineplot(x="Date", y="Sales", data=df, label="Sales")
sns.lineplot(x="Date", y="7_day_MA", data=df, label="7-day MA")

plt.scatter(top_growth["Date"], top_growth["Sales"])

plt.title("Sales Trend with Moving Average")
plt.xticks(rotation=45)
plt.show()
