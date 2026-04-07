# You are given a dataset of student marks.
# Use NumPy to generate 50 random marks between 40 and 100.
# Convert this into a Pandas DataFrame with a column named "Marks".
# Create another column "Result":
# "Pass" if marks ≥ 50
# "Fail" if marks < 50
# Using Seaborn, plot a count plot showing the number of Pass vs Fail students.
# Using Matplotlib, display a histogram of the marks distribution.


#solution 
import numpy as npa
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

marks = np.random.randint(40, 101, 100)
print(marks)

print()

df = pd.DataFrame(marks, columns=["Marks"])

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x>=50 else "Fail")

sns.countplot(x="Result", data=df)
plt.title("Pass vs Fail")
plt.show()

plt.hist(df["Marks"], bins=50)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
