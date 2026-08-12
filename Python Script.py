import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

# Set plot style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 11})

# 1. Load Data
df = pd.read_csv('Sales_Details_Raw_Data.csv')

# 2. Plot 1: Correlation Heatmap
plt.figure(figsize=(8, 6))
numeric_df = df.drop(columns=['State'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='Blues', fmt='.3f', linewidths=0.5)
plt.title('Correlation Heatmap - Startup Financial Metrics', fontsize=14, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300)
plt.close()

# 3. Plot 2: Spending vs Profit Pairwise Scatter
fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
spending_cols = ['RD_Spend', 'Administration', 'Marketing_Spend']
titles = ['R&D Spend vs Profit', 'Administration Spend vs Profit', 'Marketing Spend vs Profit']

for ax, col, title in zip(axes, spending_cols, titles):
    sns.regplot(data=df, x=col, y='Profit', ax=ax, scatter_kws={'alpha':0.7, 'color':'#1f77b4'}, line_kws={'color':'#d62728'})
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel(f'{col} ($)', fontsize=10)
    ax.set_ylabel('Profit ($)', fontsize=10)

plt.tight_layout()
plt.savefig('spending_vs_profit.png', dpi=300)
plt.close()

# 4. Regression Model
X = df[['RD_Spend', 'Administration', 'Marketing_Spend']]
y = df['Profit']

# OLS Summary
X_ols = sm.add_constant(X)
model = sm.OLS(y, X_ols).fit()
print(model.summary())

# Scikit-learn predictions for visualization
lr = LinearRegression()
lr.fit(X, y)
y_pred = lr.predict(X)

# 5. Plot 3: Actual vs Predicted Profit
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, color='#2ca02c', alpha=0.8, edgecolors='k', s=60, label='Startups')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Perfect Fit (Identity Line)')
plt.xlabel('Actual Profit ($)', fontsize=11, fontweight='bold')
plt.ylabel('Predicted Profit ($)', fontsize=11, fontweight='bold')
plt.title('Actual vs Predicted Startup Profit', fontsize=14, fontweight='bold', pad=12)
plt.legend()
plt.tight_layout()
plt.savefig('actual_vs_predicted.png', dpi=300)
plt.close()

print("Images successfully created!")