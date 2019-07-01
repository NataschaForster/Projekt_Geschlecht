import pandas as pd
import numpy as np
import glob
#CONFIGURE CONSOLE PROPERTIES
DESIRED_WIDTH = 320
pd.set_option('display.width', DESIRED_WIDTH)
np.set_printoptions(linewidth=DESIRED_WIDTH)
pd.set_option('display.max_columns', 15)
pd.options.display.max_rows = None
pd.set_option('max_colwidth', 300)

#CREATING A DATAFRAME
for i in range(0, 54):
    df = pd.read_csv('datasets/originaldaten/whole_data.csv', sep=';', low_memory=False, nrows=20000, skiprows=range(1, i*20000))
    male = df[df.ANREDE == 1]
    male.to_csv("datasets/male{}.format(i)")
    female = df[df.ANREDE == 0]
    female.to_csv("datasets/female{}.format(i)")
    print(i)

#putting em back together
path = r'C:\Projekt\projekt_geschlecht'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    gdf = pd.read_csv(filename, index_col=None, header=0)
    li.append(gdf)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv("datasets/data_with_gender")
