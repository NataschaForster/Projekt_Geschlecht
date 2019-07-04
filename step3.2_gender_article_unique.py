import pandas as pd
import glob


df = pd.read_csv("datasets/preprocessing3.1_genderspecific_clothing/preprocessing_genderspecific_article.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)


'''''''''
#FUNCTION FOR NEW COLUMN: CHECKING IF LOOKED FOR CLOTHING FOR BOTH GENDER
def content_unique_session():
    temp_df = pd.read_csv("datasets/preprocessing3.1_genderspecific_clothing/preprocessing_genderspecific_article.csv", usecols=['SESSION_ID', 'CONTENT_NAME', 'CLOTHING_GENDER', 'CLOTHING_GENDER_UNIQUE'], error_bad_lines=False, header=0, sep=';', low_memory=False)
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
'''''''''

#SPLITING DATASET IN SMALLER SETS WITH ONLY ONE SESSION EACH AND FILLING THE LAST COLUMN
def content_unique_session_separate_csv ():
    unique_session_list = df['SESSION_ID'].unique()

    for i in range(0, len(unique_session_list)):
        counter = 1

        for session in unique_session_list:
            reset = df.reset_index()
            rows_list = reset[reset["SESSION_ID"] == session].index.tolist()
            rows_df = pd.DataFrame(rows_list)
            temp_list = []

            for index in rows_df:
                row = df.iloc[index]
                print(row)
                print(type(row))
                temp_list.append(row)
                print(len(temp_list))

            temp_df = pd.DataFrame(temp_list)
            temp_df.to_csv("datasets/preprocessing3.2_gender_clothing_unique/all_sessions/session{}.csv".format(counter),sep=';', index=False)
            counter = counter + 1

    '''''''''
    #path = r'C:\Projekt\projekt_geschlecht2\datasets\preprocessing3_gendered_clothing'
    #all_files = glob.glob(path + "/*.csv")


    for file in all_files:
        df = pd.read_csv(file)
        value = df['CLOTHING_GENDER']
        
        for i in range(0, file.count()):
            if value.iloc[i, int( == 0:
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
'''''''''


#df['CLOTHING_GENDER_UNIQUE'] = content_unique_session()
content_unique_session_separate_csv()

#df.to_csv("datasets/preprocessing3.2_gender_clothing_unique/all_sessions_with_gender.csv", sep=';', index=False)
print("dataframe to csv done")