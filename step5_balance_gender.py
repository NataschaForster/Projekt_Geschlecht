# IMPORT BOUNDARIES
import pandas as pd

# LOAD DATA
df = pd.read_csv("datasets/preprocessing3.3_numeric_columns/numeric_columns_only.csv", error_bad_lines=False, sep=';', low_memory=False)

# GET ALL MALE AND FEMALE ROWS
male = df[df.ANREDE == 1]
female = df[df.ANREDE == 0]

# SHORTEN FEMALE TO THE LENGTH OF MALE
print(male.count()) #85872
female = female[:85872]
print(female.count())

# APPEND BOTH LISTS
female = female.append(male)

# CREATE NEW CSV
female.to_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", sep=';', index=False)
