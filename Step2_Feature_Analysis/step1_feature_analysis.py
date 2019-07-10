import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm as cm
import seaborn as sns

df2 = pd.read_csv("C:\Projekt\projekt_geschlecht2/datasets/preprocessing4_normalize/normalized_data.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)
df = pd.read_csv("C:\Projekt\projekt_geschlecht2/datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)



# PLOT CORRELATION MATRIX WITH NORMALIZED DATA
fig = plt.figure()
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('jet', 30)
cax = ax1.imshow(df.corr(), cmap=cmap)
plt.title('Column Correlation')
ax1.set_xticklabels(df.corr().columns, fontsize=6)
ax1.set_yticklabels(df.corr().columns, fontsize=6)
plt.show()
