import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

# NORMALIZE DATA AND GET RID OF OUTLIERS
column_list = df.columns.tolist()

for column in column_list:
    if column != 'CLOTHING_GENDER_UNIQUE' or 'COMBINED_GENDER' or 'ANREDE':  #this column should not get normalized
        column_df = df[column]
        column_df_list = list(preprocessing.normalize([column_df])[0])

        df[column] = pd.Series(column_df_list)

df.to_csv("datasets/preprocessing4_normalize/normalized_data.csv", sep=';', index=False)
