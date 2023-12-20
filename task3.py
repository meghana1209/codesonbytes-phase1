pip install seaborn matplotlib pandas
#Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/dataset - netflix1 (2).csv')

# Explore the data
print(df.info())
print(df.head())

# Example 1: Countplot
sns.countplot(x='show_id', data=df)
plt.title('Countplot Example')
plt.show()

# Example 2: Scatterplot
sns.scatterplot(x='release_year', y='duration', data=df)
plt.title('Scatterplot Example')
plt.show()

# Example 3: Barplot
sns.barplot(x='release_year', y='duration', data=df)
plt.title('Barplot Example')
plt.show()

# Example 4: Boxplot
sns.boxplot(x='release_year', y='duration', data=df)
plt.title('Boxplot Example')
plt.show()

# Example 5: Pairplot (for exploring relationships between multiple variables)
sns.pairplot(df)
plt.suptitle('Pairplot Example', y=1.02)
plt.show()
