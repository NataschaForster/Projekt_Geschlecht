import pandas as pd

df = pd.read_csv("datasets/preprocessing2_filling_empty_cells/preprocessed_mean.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

#NEW COLUMN WITH "WATCHED WOMENS/MENS CLOTHING" BY SEARCHING IN URL STRING
def gender_article(s):
    content_list = s.to_list()
    word_list_damen = ["Damen", "BHs", "Kleider", "Blusen"]
    new_column_list = []
    counter = 0
    counter_herren = 0

    for line in content_list:
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


#FUNCTION FOR NEW COLUMN: CHECKING IF LOOKED FOR CLOTHING FOR BOTH GENDER
def content_unique_session(clothing_gender, session):
    tdf = pd.DataFrame(clothing_gender, session)
    unique_session_list = session.unique().to_list()
    session_list = session.to_list()
    clothing_list = clothing_gender.to_list()
    new_column_list = []

    bool_damen = False
    bool_herren = False

    for session in unique_session_list:
        session in tdfg





    if bool_damen and bool_herren:  # funktioniert nur für eine Reihe, muss auf ganze Session angewandt werden (how?)
        new_column_list.append(3)
    else:
        new_column_list.append(element)

 '''''''''
df['CLOTHING_GENDER_UNIQUE'] = content_unique_session(df['CLOTHING_GENDER'].astype(int), df['SESSION_ID'].astype(str))

#df.to_csv("datasets/preprocessing3_gendered_clothing/preprocessing_gender_article.csv", sep=';', index=False)
print("dataframe to csv done")