import pandas as pd
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
            list_prepared.append(float(0))
    return pd.Series(list_prepared)

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

#WRITING A NEW CSV
df.to_csv("datasets/preprocessed_zero.csv", sep=';', index=False, header=0)


#FUNCTION REPLACING 0 WITH MEAN

#calculating the mean of the used columns
#which columns are worth replacing with the mean?
mean_view = float(df['VIEWTIME_IN_S'].mean())
mean_groesse = float(df['GROESSE'].mean()) # equals 0, so irrelevant
mean_absatz = float(df['ABSATZ'].mean())
mean_pprice = float(df['PPRICE'].mean()) # equals 0, so irrelevant
mean_bestellsumme = float(df['BESTELLSUMME'].mean()) # equals 0, so irrelevant
mean_coupon = float(df['COUPONWERT'].mean()) # equals 0, so irrelevant
mean_anzahl = float(df['ANZAHL'].mean()) #MACHT DIESER WERT SINN?_____________________________________________________________________________

mean_list = [mean_view, mean_groesse, mean_absatz, mean_pprice, mean_bestellsumme, mean_coupon, mean_anzahl]
print(mean_list)
relevant_means = [mean_view, mean_absatz, mean_anzahl]

#function
def replaceMean(s, mean):

    column_list = s.to_list()
    list_with_mean = []

    for element in column_list:
        if element == 0:
            list_with_mean.append(float(mean))
        else:
            list_with_mean.append(float(element))
    return pd.Series(list_with_mean)



#REPLACING ALL RELEVANT MEANS
df['VIEWTIME_IN_S'] = replaceMean(df['VIEWTIME_IN_S'], float(df['VIEWTIME_IN_S'].mean()))
df['ABSATZ'] = replaceMean(df['ABSATZ'], float(df['ABSATZ'].mean()))
df['ANZAHL'] = replaceMean(df['ANZAHL'], float(df['ABSATZ'].mean()))

#WRITING A NEW CSV
df.to_csv("datasets/preprocessed_mean.csv", sep=';', index=False, header=0)

