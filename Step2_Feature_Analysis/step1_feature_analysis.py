import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm as cm
import seaborn as sns

df2 = pd.read_csv("C:\Projekt\projekt_geschlecht2/datasets/preprocessing4_normalize/normalized_data.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)
df = pd.read_csv("C:\Projekt\projekt_geschlecht2/datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

# PLOT CORRELATION MATRIX WITH NORMALIZED DATA

print(df2.isnull().sum())
correlation = df2.corr()
sns.heatmap(correlation.isnull(), yticklabels=False, annot=True, )
plt.show()


