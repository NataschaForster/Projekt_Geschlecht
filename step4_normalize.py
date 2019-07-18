# IMPORT BOUNDARIES
import pandas as pd
from sklearn import preprocessing

# LOAD DATA
df = pd.read_csv("datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

# LIST OF COLUMNS
column_list = df.columns.tolist()

# NORMALIZE DATA AND GET RID OF OUTLIERS
for column in column_list:
    if column != 'CLOTHING_GENDER_UNIQUE' or 'COMBINED_GENDER' or 'ANREDE':  #this columnS should not get normalized
        column_df = df[column]
        column_df_list = list(preprocessing.normalize([column_df])[0])

        df[column] = pd.Series(column_df_list)

# CREATE NEW CSV
df.to_csv("datasets/preprocessing4_normalize/normalized_data.csv", sep=';', index=False)
