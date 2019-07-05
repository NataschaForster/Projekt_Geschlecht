import pandas as pd


#HIER DATEI AUS 3.2 VERWENDEN!!!
df = pd.read_csv("datasets/preprocessing2_filling_empty_cells/preprocessed_mean.csv", error_bad_lines=False, sep=';', low_memory=False)
num_df = pd.DataFrame()
numeric_columns = pd.DataFrame(df.loc[:, [[df['ABSATZ'], df['PPRICE'], df['GROESSE'], df['BESTELLSUMME'], df['COUPONWERT'], df['MARKTKENNZEICHEN']]]]) #, df['CLOTHING_GENDER'], df['CLOTHING_GENDER_UNIQUE']
print('got numeric columns')

#GETTING A NEW DATA FRAME WITH ONLY IMPORTANT/NUMERIC COLUMNS
num_df = pd.DataFrame(numeric_columns)
print('df created')

num_df.to_csv("datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", sep=';', index=False)
