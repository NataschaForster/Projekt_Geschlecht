import pandas as pd
import numpy as np
import math

#SCANNING DATASET
df = pd.read_csv('datasets/dataset_with_gender.csv', error_bad_lines=False, header=0, sep=';', low_memory=False)

#FUNCTION REPLACING NAN WITH 0 IN COLUMNS
def cleanSeries(s):
    list = s.to_list()
    list_prepared = []

    for element in list:
        try:

            if math.isnan(element):
                list_prepared.append(float(0))

            else:
                cleared_num = str(element).replace("/", '.').replace(",", '.')
                list_prepared.append(float(cleared_num))

        except Exception as e:
            print(e)
            list_prepared.append(float(0))
    return pd.Series(list_prepared)

#FUNCTION REPLACING 0 WITH MEAN
def replaceMean(s):
    list = s.to_list()
    list_with_mean = []

    for element in list:
        if element == 0:
            list_with_mean.append(float(s.mean()))
            print("if")
        else:
            list_with_mean.append(float(element))
            print("else")
    return pd.Series(list_with_mean)


#FILLING THE DATAFRAME WITH 0
df['VIEWTIME_IN_S'] = cleanSeries(df['VIEWTIME_IN_S'])
df['ABSATZ'] = cleanSeries(df['ABSATZ'])
df['PPRICE'] = cleanSeries(df['PPRICE'])
df['GROESSE'] = cleanSeries(df['GROESSE'])
df['BESTELLSUMME'] = cleanSeries(df['BESTELLSUMME'])
df['COUPONWERT'] = cleanSeries(df['COUPONWERT'])
df['PROMOTIONNR'] = cleanSeries(df['PROMOTIONNR'])
df['MARKTKENNZEICHEN'] = cleanSeries(df['MARKTKENNZEICHEN'])
df['ARTIKELNR'] = cleanSeries(df['ARTIKELNR'])
df['ANZAHL'] = cleanSeries(df['ANZAHL'])
df['ARTIKELNR'] = cleanSeries(df['ARTIKELNR'])

#REPLACING SOME MISSING VALUES WITH THE COLUMN MEAN
df['VIEWTIME_IN_S'] = replaceMean(df['VIEWTIME_IN_S'])
print("doneeeeeeeeeeeeeeeeeeeeeeeeeeeee")
df['ABSATZ'] = replaceMean(df['ABSATZ'])
print("doneeeeeeeeeeeeeeeeeeeeeeeeeeeee")
df['PPRICE'] = replaceMean(df['PPRICE'])
print("doneeeeeeeeeeeeeeeeeeeeeeeeeeeee")
df['GROESSE'] = replaceMean(df['GROESSE'])
print("doneeeeeeeeeeeeeeeeeeeeeeeeeeeee")

#WRITING A NEW CSV
df.to_csv("datasets/preprocessed_1.csv", sep=';')
