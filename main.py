import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob
import os
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

#SIMPLE STATS NOT NORMALISED
dfCensus3 = pd.read_csv("Census2022V3.0Normalised.csv")

# Summary statistics
summary = dfCensus3.describe().T[['mean', '50%', 'std']]  # 50% = median
summary.rename(columns={'50%': 'median'}, inplace=True)
print(summary)

# Select only numeric columns
all_columns = dfCensus3.columns

# Compute correlations
correlation_matrix = dfCensus3[all_columns].corr()

# Show correlation of age groups with 'No. Cars'
print(correlation_matrix['Total BEVs'].sort_values(ascending=False))

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Census Data Groups and BEV Registration")
plt.show()

# Create scatterplots for each age group
import matplotlib.pyplot as plt
import seaborn as sns

for col in all_columns:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=dfCensus3[col], y=dfCensus3['Total BEVs'])
    sns.regplot(x=dfCensus3[col], y=dfCensus3['Total BEVs'], scatter=False, color='red')
    plt.title(f"Total BEVs Reg. vs {col}")
    plt.xlabel(col)
    plt.ylabel("Total BEVs Re.")
    plt.tight_layout()
    plt.show()