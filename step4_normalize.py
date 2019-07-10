import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import numpy as np

df = pd.read_csv("datasets/preprocessing3.3_only_numeric_columns/numeric_columns_only.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

# PLOT EACH COLUMN AND ALL COLUMNS CORRELATED WITH EACH OTHER
sns.set(style="ticks", color_codes=True)
g = sns.pairplot(df)

# NORMALIZE DATA AND GET RID OF OUTLIERS
column_list = df.column.tolist()

for column in column_list:
    column_array = np.array(df[column])
    normalized_column = preprocessing.normalize([column_array])

    df[column] = normalized_column

df.to_csv("datasets/preprocessing4_normalize/normalized_data.csv", sep=';', index=False)
