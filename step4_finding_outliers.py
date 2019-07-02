import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("datasets/preprocessing3_gendered_clothing/preprocessing_gender_article.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

#LIST OF ALL NUMERIC COLUMNS9
#viewtime missing
numeric_columns = [df['ABSATZ'], df['PPRICE'], df['GROESSE'], df['BESTELLSUMME'], df['COUPONWERT'], df['PROMOTIONNR'], df['MARKTKENNZEICHEN'], df['ARTIKELNR'], df['ANZAHL'], df['ARTIKELNR']]

#VISUALIZING THE DISTRIBUTION OF NUMERIC COLUMNS
for column in numeric_columns:
    sns.distplot(column.astype(float));

#DELETING OUTLiERS
for column in numeric_columns:
    print("1")
