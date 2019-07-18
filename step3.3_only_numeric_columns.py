# IMPORT BOUNDARIES
import pandas as pd

# LOAD DATA
df = pd.read_csv("datasets/preprocessing3.2_gender_clothing_unique/combined_gender_5columns.csv", error_bad_lines=False, sep=';', low_memory=False)

# NEW DATAFRAME WITH ONLY SOME NUMERIC COLUMNS
numeric_columns = pd.DataFrame(df[['ANREDE', 'ANZAHL', 'ABSATZ', 'PPRICE', 'GROESSE', 'BESTELLSUMME', 'COUPONWERT',
                                   'MARKTKENNZEICHEN', 'VIEWTIME_IN_S', 'COMBINED_GENDER', 'CLOTHING_GENDER_UNIQUE',
                                   'CLOTHING_GENDER', 'SEARCH_GENDER', 'SEARCH_GENDER_UNIQUE']])

# GETTING A NEW DATA FRAME WITH ONLY IMPORTANT/NUMERIC COLUMNS
num_df = pd.DataFrame(numeric_columns)

# CREATING NEW CSV
num_df.to_csv("datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", sep=';', index=False)
