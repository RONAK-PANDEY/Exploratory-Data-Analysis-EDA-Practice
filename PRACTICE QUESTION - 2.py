# The Challenge: Employee Performance Analysis
# The Question
# Generate Data: Create a NumPy array of 100 random integers representing "Hours Worked" (between 30 and 50).
# Process Data: Create a Pandas DataFrame with two columns: Hours_Worked and Efficiency_Score. The Efficiency_Score should be the Hours_Worked multiplied by a factor of 1.5.
# Visualize: Create a Scatter Plot using Seaborn to show the relationship between hours and efficiency, and add a custom title using Matplotlib

#solution 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hours = np.random.randint(30, 51, 100)

print(hours)

print()

df = pd.DataFrame({'Hours_Worked':hours, 'Efficiency_Score': hours * 1.5})

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Hours_Worked', y='Efficiency_Score', color='teal')

plt.title('Hours Worked vs. Efficiency Score', fontsize=14)
plt.xlabel('Hours Worked')
plt.ylabel('Efficiency Score')
plt.grid(True, linestyle='solid', alpha=1) 
plt.show()
