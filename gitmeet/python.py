import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/nages/Documents/world_population.csv')

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# Display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())

# Plot histograms for each numeric column
df.hist(figsize=(10, 8))
plt.suptitle('Histograms of Numeric Columns')
plt.tight_layout()  # Adjust subplots to fit into figure area.
plt.show()

# Plot a correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()  # Adjust subplots to fit into figure area.
plt.show()

# Plot pairplot for the DataFrame
pairplot_fig = sns.pairplot(df)
pairplot_fig.fig.suptitle('Pairplot of DataFrame', y=1.02)
plt.show()

# Save the statistics to a CSV file
df.describe().to_csv('statistics.csv')