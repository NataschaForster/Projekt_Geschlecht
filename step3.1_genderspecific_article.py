import pandas as pd

df = pd.read_csv("datasets/preprocessing2_filling_empty_cells/preprocessed_mean.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

#NEW COLUMN WITH "WATCHED WOMENS/MENS CLOTHING" BY SEARCHING IN URL STRING
def gender_article(s):
    content_list = s.to_list()
    word_list_damen = ["Damen", "damen" "BHs", "Kleider", "Blusen"]
    word_list_herren = ["Herren", "herren", "Pollunder", "Boxershorts"]
    new_column_list = []
    counter = 0
    counter_herren = 0

    for line in content_list:
        for word in word_list_damen:
            if str(word) in str(line):
                counter = counter + 1
        for word in word_list_herren:
            if str(word) in str(line):
                counter_herren += 1

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
df.to_csv("datasets/preprocessing3.1_genderspecific_clothing/preprocessing_genderspecific_article.csv", sep=';', index=False)

