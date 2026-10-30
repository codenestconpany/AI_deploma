import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

np.random.seed(42)

data = {
    'Employee_ID': np.arange(201, 231),
    'Department': np.random.choice(['Sales', 'IT', 'HR', 'Marketing'], size=30),
    'Age': np.random.choice([22, 25, 28, 32, 35, 40, 45, np.nan], size=30),
    'Salary': [4500, 8200, 6100, 7000, 8100, 9500, np.nan, 8300, 4900, 10500,
               5200, 8800, 6300, np.nan, 8000, 9200, 11200, 8100, 4700, 10800,
               5100, 8600, 6000, 7200, 8300, np.nan, 11500, 8400, 5000, 10200],
    'Experience_Years': [1, 6, 3, 5, 4, 8, 15, 6, 2, 12,
                        2, 7, 3, np.nan, 4, 9, 16, 5, 1, 14,
                        2, 7, 3, 6, 5, 10, 17, 6, 1, 13],
    'Performance_Score': np.random.randint(65, 100, size=30)
}

df = pd.DataFrame(data)

print(df.head())
print(df.tail())

print(df.info())
print(df.isnull().sum())

df['Salary'] = df.groupby('Department')['Salary'].transform(lambda x: x.fillna(x.mean()))
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Experience_Years'] = df['Experience_Years'].fillna(df['Experience_Years'].median())

print(df.isnull().sum())

salary_mean = df['Salary'].mean()
salary_median = df['Salary'].median()
salary_std = df['Salary'].std()
salary_range = df['Salary'].max() - df['Salary'].min()

print(f"Mean: {salary_mean:.2f}")
print(f"Median: {salary_median:.2f}")
print(f"Standard Deviation: {salary_std:.2f}")
print(f"Range: {salary_range:.2f}")

df['Bonus'] = np.where(df['Performance_Score'] > 85, df['Salary'] * 0.12, df['Salary'] * 0.05)
df['Total_Compensation'] = df['Salary'] + df['Bonus']

dept_summary = df.groupby('Department').agg(
    Avg_Total_Compensation=('Total_Compensation', 'mean'),
    Max_Performance_Score=('Performance_Score', 'max'),
    Min_Performance_Score=('Performance_Score', 'min')
).reset_index()

print(dept_summary)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.barplot(data=df, x='Department', y='Total_Compensation', ax=axes[0], palette='Blues_d', errorbar=None)
axes[0].set_title('Average Total Compensation by Department')
axes[0].set_xlabel('Department')
axes[0].set_ylabel('Total Compensation')

sns.scatterplot(data=df, x='Experience_Years', y='Salary', hue='Department', ax=axes[1], s=80)
sns.regplot(data=df, x='Experience_Years', y='Salary', ax=axes[1], scatter=False, color='red')
axes[1].set_title('Salary vs Experience Years')
axes[1].set_xlabel('Experience Years')
axes[1].set_ylabel('Salary')

sns.boxplot(data=df, x='Department', y='Performance_Score', ax=axes[2], palette='Set2')
axes[2].set_title('Performance Score Distribution by Department')
axes[2].set_xlabel('Department')
axes[2].set_ylabel('Performance Score')

plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
numeric_cols = df[['Age', 'Salary', 'Experience_Years', 'Performance_Score', 'Total_Compensation']]
sns.heatmap(numeric_cols.corr(), annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()