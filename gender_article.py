import pandas as pd

df = pd.read_csv("datasets/preprocessing2_filling_empty_cells/preprocessed_mean.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

#NEW COLUMN WITH "WATCHED WOMENS/MENS CLOTHING" BY SEARCHING IN URL STRING
def gender_article(s):
    column_list = s.to_list()
    word_list_damen = ["Damen", "BHs", "Kleider", "Blusen"]
    new_column_list = []
    counter = 0
    counter_herren = 0
    for line in column_list:
        for word in word_list_damen:
            if "Herren" in str(line):
                counter_herren = counter_herren + 1
            if str(word) in str(line):
                counter = counter + 1

        if counter_herren > 0:
            new_column_list.append(0)#masculine clothing
        elif counter > 0:
            new_column_list.append(1) #feminine clothing
        else:
            new_column_list.append(2) #no gendered clothing
            
        counter = 0
        counter_herren = 0

    return pd.Series(new_column_list)


df['CLOTHING_GENDER'] = gender_article(df['CONTENT_NAME'].astype(str))
print("checked for gender clothing")
df.to_csv("datasets/preprocessing3_gendered_clothing/preprocessing_gender_article.csv", sep=';', index=False)
print("dataframe to csv done")
