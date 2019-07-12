import pandas as pd

df = pd.read_csv("datasets/preprocessing3.2_gender_clothing_unique/whole_data.csv", error_bad_lines=False, sep=';', low_memory=False)

male = df[df.ANREDE == 1]
female = df[df.ANREDE == 0]

print(male.count()) #51366
female = female[:51366]
print(female.count())

female = female.append(male)

female.to_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", sep=';', index=False)
