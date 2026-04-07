# The Challenge: Identifying Top-Performing Engineers
# The Question
# Generate Data: Create a NumPy array of 500 records representing "Lines of Code" (LOC) written by developers, following a normal distribution (mean=500, std=150).
# Logic (The "LeetCode" part):
# Create a Pandas DataFrame.
# Filter: Remove any "bugs" (records where LOC is less than 100).
# Transformation: Create a new column Category. If LOC > 700, label it "Senior"; between 400-700, "Mid-level"; below 400, "Junior".
# Visualisation:
# Use Seaborn to create a box plot showing the distribution of LOC across these three Category types.
# Use Matplotlib to annotate the plot with a horizontal line representing the average LOC across the entire company.

np.random.seed(43)
loc_data = np.random.normal(500, 150, 500)

df = pd.DataFrame({'LOC': loc_data})

df = df[df['LOC'] >= 100]

def classify_dev(loc):
    if loc > 700:
        return 'Senior'
    elif loc >= 400:
        return 'Mid-level'
    else:
        return 'Junior'
        
df['Category'] = df['LOC'].apply(classify_dev)    

plt.figure(figsize=(10, 6))

sns.boxplot(data=df, x='Category', y='LOC', hue='Category', palette='Set2', order=['Junior', 'Mid-level', 'Senior'])

avg_loc = df['LOC'].mean()
plt.axhline(avg_loc, color='red', linestyle='--', label=f'Company Avg: {avg_loc:.2f}')

plt.title('Developer Productivity Distribution by Rank', fontsize=15)
plt.legend() 
plt.show()
