import pandas as pd
import glob
import shutil
import os

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

# SPLITING DATASET IN SMALLER SETS WITH ONLY ONE SESSION EACH AND FILLING THE LAST COLUMN
def content_unique_session_separate_csv ():
    unique_session_list = df['SESSION_ID'].unique()
    counter = 0

    for session in unique_session_list:

        reset = df.reset_index()

        session_row_ids = reset[reset["SESSION_ID"] == session].index.tolist() # muss session hier nicht mit df  interagieren?
        temp_df = pd.DataFrame()
        new_column_list = []

        bool_damen = False
        bool_herren = False

        for index in session_row_ids:
            row = pd.Series(reset.iloc[index])
            temp_df = temp_df.append(row)

        for index in range(0, len(temp_df)):
            row = temp_df.iloc[index]
            value = row['CLOTHING_GENDER']

            if value == 1:
                bool_damen = True
            elif value == 0:
                bool_herren = True

        if bool_damen and bool_herren:
            for i in range(0, len(temp_df['CLOTHING_GENDER_UNIQUE'])):
                new_column_list.append(3)
        elif bool_damen and not bool_herren:
            for i in range(0, len(temp_df['CLOTHING_GENDER_UNIQUE'])):
                new_column_list.append(1)
        elif bool_herren and not bool_damen:
            for i in range(0, len(temp_df['CLOTHING_GENDER_UNIQUE'])):
                new_column_list.append(0)
        else:
            for i in range(0, len(temp_df['CLOTHING_GENDER_UNIQUE'])):
                new_column_list.append(2)

        temp_df['CLOTHING_GENDER_UNIQUE'] = new_column_list

        counter = counter + 1
        print("{} csv done".format(session))
        temp_df.to_csv("datasets/preprocessing3.2_gender_clothing_unique/all_sessions/session{}.csv".format(counter), sep=';', index=False)


# DELETING OLD CSVS AND CREATING FOLDER
path2 = "datasets/preprocessing3.2_gender_clothing_unique/all_sessions"

try:

    shutil.rmtree(path2)
except:
    print("folder is removed")

try:
    os.mkdir(path2)
except OSError:
    print("Creation of the directory %s failed" % path2)
else:
    print("Successfully created the directory %s " % path2)

# CREATE SMALL CSVS
content_unique_session_separate_csv()


# CONCATENATING ALL FILES BACK TOGETHER
path1 = r'C:\Projekt\projekt_geschlecht2\datasets\preprocessing3.2_gender_clothing_unique\all_sessions'
all_files = glob.glob(path1 + "/*.csv")

li = []

for filename in all_files:
    try:
        df = pd.read_csv(filename, index_col=None, header=0, sep=';', low_memory=False)
        li.append(df)

    except Exception as e:
        print(e)
        print(filename)

print('creating final dataset')
frame = pd.concat(li, axis=0, ignore_index=True, sort=True)
frame.to_csv("datasets/preprocessing3.2_gender_clothing_unique/whole_dataset.csv", sep=';', index=False)
