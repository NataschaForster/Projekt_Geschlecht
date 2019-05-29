import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creating dataframe
df = pd.read_csv('datasets/originaldaten/whole_data.txt')
print(df.head())

#saving all females in data field
#fem = len(df[df['GESCHLECHT'] == 'female'])
#print(fem)

#replace empty fields with NaN
#print(df.replace(r'^\s*$', np.nan, regex=True))
df.fillna(method='ffill')
print(df.head())

#correlation
print(df.corr())

#plot some things
#plt.boxplot(df['GROESSE'])
df.plot()
