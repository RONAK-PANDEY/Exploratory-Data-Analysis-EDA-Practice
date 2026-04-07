# You are given student marks again, but now think like a data analyst + problem solver:
# Use NumPy to generate 100 random marks between 0 and 100.
# Create a Pandas DataFrame with column "Marks".
# Create a "Grade" column using logic:
# 90–100 → "A"
# 75–89 → "B"
# 50–74 → "C"
# Below 50 → "F"
# Find:
# The average marks of each grade
# The number of students in each grade
# Using Seaborn, plot:
# A bar plot of average marks per grade
# Using Matplotlib, plot:
# A line plot of sorted marks (ascending)

#solution 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Marks = np.random.randint(0, 101, 100)
print(Marks)

print()

df = pd.DataFrame(Marks, columns=["Marks"])

def assign_grades(x):
    if x >= 90:
        return"A"
    elif x >= 75:
        return "B"
    elif x >= 50:
        return "C"
    else:
        return "F"

df["Grades"] = df["Marks"].apply(assign_grades)

avg_marks = df.groupby("Grades")["Marks"].mean()
count_students = df["Grades"].value_counts()

print("Average Marks per Grade:\n", avg_marks)
print("\nStudent Count per Grade:\n", count_students)

sns.barplot(x=avg_marks.index, y=avg_marks.values)
plt.title("Average Marks per Grade")
plt.show()

sorted_marks = df["Marks"].sort_values().reset_index(drop=True)

plt.plot(sorted_marks)
plt.title("Sorted Marks Line Plot")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()
