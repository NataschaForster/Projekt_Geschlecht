import pandas as pd
import numpy as np

#SCANNING DATASET
df = pd.read_csv('datasets/dataset_with_gender.csv', error_bad_lines=False, header=0, sep=';')

#FUNCTION CLEANING COLUMNS
def cleanSeries(s):
    list = s.to_list()
    list_prepared = []

    for size in list:
        try:
            cleared_num = str(size).replace("/", '.', inplace=True).replace(",", '.', inplace=True)
            list_prepared.append(float(cleared_num))
        except Exception as e:
            list_prepared.append(float(0))
    return pd.Series(list_prepared)

#CALCULATING 4 MEANS
meanViewtime = cleanSeries(df['VIEWTIME_IN_S']).mean()
meanAbsatz = cleanSeries(df['ABSATZ']).mean()
meanPrice = cleanSeries(df['PPRICE']).mean()
meanGroesse = cleanSeries(df['GROESSE']).mean()
