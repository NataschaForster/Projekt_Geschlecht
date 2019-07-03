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
df.to_csv("datasets/preprocessing3_gendered_clothing/preprocessing_gender_article.csv", sep=';', index=False)



#FUNCTION FOR NEW COLUMN: CHECKING IF LOOKED FOR CLOTHING FOR BOTH GENDER
#alles nur notizen bisher
df = pd.read_csv("datasets/preprocessing3_gendered_clothing/preprocessing_gender_article.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

def content_unique_session():
    temp_df = pd.read_csv("datasets/preprocessing3_gendered_clothing/preprocessing_gender_article.csv", usecols=['SESSION_ID', 'CONTENT_NAME', 'CLOTHING_GENDER', 'CLOTHING_GENDER_UNIQUE'], error_bad_lines=False, header=0, sep=';', low_memory=False)
    new_column_list = []
    unique_session_list = temp_df['SESSION_ID'].unique()
    print("unique")
    print(type(temp_df))
    counter = 0

    #GETTING INDICES OF ROWS BELONGING TO SESSION
    for session in unique_session_list:
        reset = temp_df.reset_index()
        bool_damen = False
        bool_herren = False
        rows_with_session_index = reset[reset["SESSION_ID"] == session].index.tolist()


        #CHECKING IF LOOKED AT GENDER SPECIFIC CLOTHING

        len_session = len(rows_with_session_index)

        for index in rows_with_session_index:
            value = temp_df.iloc[index, int(2)]

            if value == 0:
                bool_damen = True
            elif value == 1:
                bool_herren = True

            if bool_damen and bool_herren:
                new_column_list.append(3)
            elif bool_damen and not bool_herren:
                new_column_list.append(0)
            elif bool_herren and not bool_damen:
                new_column_list.append(1)
            else:
                new_column_list.append(2)

        counter = counter + 1
        print(str((counter / len(unique_session_list))*100) + "%")

    return pd.Series(new_column_list)


df['CLOTHING_GENDER_UNIQUE'] = content_unique_session()


df.to_csv("datasets/preprocessing3_gendered_clothing/preprocessing_gender_article_session.csv", sep=';', index=False)
print("dataframe to csv done")

