import pandas as pd
import numpy as np

df = pd.read_csv("datasets/preprocessing3.1_genderspecific_clothing/preprocessing_genderspecific_article.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)
#numeric_columns = [df['VIEWTIME_IN_S', df['ABSATZ'], df['PPRICE'], df['GROESSE'], df['BESTELLSUMME'], df['COUPONWERT'], df['PROMOTIONNR'], df['MARKTKENNZEICHEN'], df['ARTIKELNR'], df['ANZAHL'], df['ARTIKELNR']]]

#FUNCTION TO DETECT OUTLIERS
def detect_outliers(column):
    value_list = column.tolist()
    threshold = 3
    mean = np.mean(column)
    std = np.std(column)

    for value in value_list:
        z_score = (value - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(value)

    print(len(outliers))
    return outliers


#CREATING DATASET WITH DETECTED OUTLIERS
outliers = pd.DataFrame(detect_outliers(df['VIEWTIME_IN_S']))

#GETTING IGD
sorted(df) #nach welcher Spalte wird sortiert? wenn ich eine spalte sortiere, kriege ich das df nie wieder richtig zusammen -> index mitliefern?


#VISUALIZING THE DISTRIBUTION OF NUMERIC COLUMNS
#for column in numeric_columns:

