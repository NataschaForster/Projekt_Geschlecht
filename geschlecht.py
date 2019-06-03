import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#CONFIGURE CONSOLE PROPERTIES
DESIRED_WIDTH = 320
pd.set_option('display.width', DESIRED_WIDTH)
np.set_printoptions(linewidth=DESIRED_WIDTH)
pd.set_option('display.max_columns', 15)
pd.options.display.max_rows = None
pd.set_option('max_colwidth', 300)

#CREATING A DATAFRAME
df = pd.read_csv('datasets/originaldaten/whole_data.csv', sep=';', low_memory=False)
print(df.head())

#PRINT ALL ROWS OF A SINGLE SESSION
print(df[df['SESSION_ID'] == 231413958])



#saving all females in data field
#fem = len(df[df['GESCHLECHT'] == 'female'])
#print(fem)

#replace empty fields with NaN
#print(df.replace(r'^\s*$', np.nan, regex=True))
#df.fillna(method='ffill')
#print(df.head())

#correlation
#print(df.corr())

#plot some things
#plt.boxplot(df['GROESSE'])
#x = df["ARTIKELNR"]
#y = df["PRICE"]
#plt.plot(x,y) #header gelöscht, immer noch no numeric data to plot

#manual correlation
#df.astype(float) #mögliche Problemlösung
#df['F'].corr(df['S']) #wie spreche ich die richtige Reihe an? ist die Headerzeile evtl ein Problem?
