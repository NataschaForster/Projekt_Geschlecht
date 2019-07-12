import pandas as pd

df = pd.read_csv("datasets/preprocessing3.2_gender_clothing_unique/combined_gender.csv", error_bad_lines=False, sep=';', low_memory=False)
num_df = pd.DataFrame()
numeric_columns = pd.DataFrame(df[['ANREDE', 'ANZAHL', 'ABSATZ', 'PPRICE', 'GROESSE', 'BESTELLSUMME', 'COUPONWERT', 'MARKTKENNZEICHEN', 'SEARCH_GENDER', 'SEARCH_GENDER_UNIQUE', 'VIEWTIME_IN_S', 'CLOTHING_GENDER_UNIQUE', 'CLOTHING_GENDER']])
print('got numeric columns')

# GETTING A NEW DATA FRAME WITH ONLY IMPORTANT/NUMERIC COLUMNS
num_df = pd.DataFrame(numeric_columns)
print('df created')

num_df.to_csv("datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", sep=';', index=False)
