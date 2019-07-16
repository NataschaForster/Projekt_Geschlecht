import pandas as pd

df = pd.read_csv("datasets/preprocessing3.2_gender_clothing_unique/combined_gender_5columns.csv", error_bad_lines=False, sep=';', low_memory=False)
num_df = pd.DataFrame()
numeric_columns = pd.DataFrame(df[['ANREDE', 'COMBINED_GENDER']])

# OTHER NUMERIC COLUMNS, THAT DIDNT GET PUT IN
# 'VIEWTIME_IN_S', 'CLOTHING_GENDER_UNIQUE', 'CLOTHING_GENDER', 'SEARCH_GENDER', 'SEARCH_GENDER_UNIQUE', 'ANZAHL', 'ABSATZ', 'PPRICE', 'GROESSE', 'BESTELLSUMME', 'COUPONWERT', 'MARKTKENNZEICHEN'


print('got numeric columns')

# GETTING A NEW DATA FRAME WITH ONLY IMPORTANT/NUMERIC COLUMNS
num_df = pd.DataFrame(numeric_columns)
print('df created')
print(df['COMBINED_GENDER'].count())

#sns.heatmap(num_df.corr())
#plt.show()

num_df.to_csv("datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", sep=';', index=False)
