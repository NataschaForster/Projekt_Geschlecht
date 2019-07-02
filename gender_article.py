import pandas as pd

df = pd.read_csv("datasets/preprocessed_mean.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

#NEW COLUMN WITH "WATCHED WOMENS/MENS CLOTHING" BY SEARCHING IN URL STRING
def gender_article(s):
    column_list = s.to_list()
    word_list = ["damen", "bhs", "kleider", "blusen"]
    new_column_list = []

    for line in column_list:
        for word in word_list:
            if line.str.contains(word, case=False):
                new_column_list.append(1)
                break
            else:
                new_column_list.append(0)

        return pd.Series(new_column_list)


df['CLOTHING_GENDER'] = gender_article(df['CLOTHING_GENDER'])
df.to_csv("preprocessing_gender_article.csv", sep=';', index=False)
