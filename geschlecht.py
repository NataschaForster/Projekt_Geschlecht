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

create_new = False

if create_new:
    #CHUNKING DATAFRAME INTO 108 SMALLER ONES; NO EMPTY GENDER FIELDS REMAINING
    for i in range(0, 54):
        df = pd.read_csv('datasets/originaldaten/whole_data.csv', sep=';', low_memory=False, nrows=20000, skiprows=range(1, i*20000), encoding='latin-1')
        male = df[df.ANREDE == 1]
        male.to_csv("datasets/male{}.csv".format(i), sep=';')
        female = df[df.ANREDE == 0]
        female.to_csv("datasets/female{}.csv".format(i), sep=';')
        print(i)



#CREATING ONE CSV FILE WITH THE RECENTLY CREATED ONES
path = r'C:\Projekt\projekt_geschlecht2\datasets'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    try:
        df = pd.read_csv(filename, index_col=None, header=0, sep=';')
        li.append(df)

    except Exception as e:
        print(e)
        print(filename)


frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv("datasets/dataset_with_gender.csv", sep=';')
