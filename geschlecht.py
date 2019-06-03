import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creating dataframe
df = pd.read_csv('datasets/originaldaten/data.csv') #sep='delimiter' hilft hier nicht weiter, error_bad_lines=False lässt den pc ewig arbeiten
df.columns = ['ANZAHL',	'ARTIKELNR', 'PROMOTIONNR',	'PPRICE', 'GROESSE', 'MARKTKENNZEICHEN', 'PLATTFORM', 'BROWSER', 'BROWSER_GROUP', 'ISMOBILE', 'MOBILE_VENDOR', 'MOBILE_MODEL', 'ENTRYPAGE',	'GESCHLECHT', 'KONTO_ID', 'ANREDE',	'ANREDEBEZ'
] #Reihen benennen?

print(df.head())

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
x = df["ARTIKELNR"]
y = df["PRICE"]
plt.plot(x,y) #header gelöscht, immer noch no numeric data to plot


#manual correlation
#df.astype(float) #mögliche Problemlösung
#df['F'].corr(df['S']) #wie spreche ich die richtige Reihe an? ist die Headerzeile evtl ein Problem?
