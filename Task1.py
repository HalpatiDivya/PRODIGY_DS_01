import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file path to the Titanic dataset
file_path = r'C:\Users\Admin\Downloads\archive (11)\Titanic Dataset.csv'

# Load the Titanic dataset
df = pd.read_csv(file_path)

# Handle missing values

# Replace missing 'Age' values with median age
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)

# Plotting the age distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution in Titanic Dataset')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.75)
plt.show()
