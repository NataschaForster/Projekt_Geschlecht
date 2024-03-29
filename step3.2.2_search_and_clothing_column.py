# IMPORT BOUNDARIES
import pandas as pd

# LOAD DATA
df = pd.read_csv("datasets/preprocessing3.2_gender_clothing_unique/whole_data.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)


# FUNCTION TO COMBINE ALL FOUR NEW COLUMNS
def combine_gender():
    temp_df = df
    new_column_list = []
    unique_session_list = temp_df['SESSION_ID'].unique()
    counter = 0

    # GETTING INDICES OF ROWS BELONGING TO SESSION
    for session in unique_session_list:
        reset = temp_df.reset_index()
        bool_damen = False
        bool_herren = False
        rows_with_session_index = reset[reset["SESSION_ID"] == session].index.tolist()

        # CHECKING IF LOOKED AT GENDER SPECIFIC CLOTHING
        row = temp_df.iloc[rows_with_session_index[0]]
        value = row['SEARCH_GENDER_UNIQUE']
        value2 = row['CLOTHING_GENDER_UNIQUE']

        if value == 1:
            bool_damen = True
        if value == 0:
            bool_herren = True
        if value2 == 1:
            bool_damen = True
        if value2 == 0:
            bool_herren = True

        # COMPARING WHAT HAS BEEN LOOKED AT AND THEN FILLING ALL ROWS BELONGING TO ONE SESSION WITH THE SAME NUMBER
        if bool_damen and bool_herren:
            for i in range(0, len(rows_with_session_index)):
                new_column_list.append(3)
        elif bool_damen and not bool_herren:
            for i in range(0, len(rows_with_session_index)):
                new_column_list.append(1)
        elif bool_herren and not bool_damen:
            for i in range(0, len(rows_with_session_index)):
                new_column_list.append(0)
        else:
            for i in range(0, len(rows_with_session_index)):
                new_column_list.append(2)

        counter = counter + 1
        print(str((counter / len(unique_session_list))*100) + "%")

    return pd.Series(new_column_list)


# FILL NEW COLUMN
df['COMBINED_GENDER'] = combine_gender()

# CREATE NEW CSV
df.to_csv("datasets/preprocessing3.2_gender_clothing_unique/combined_gender_5columns.csv", sep=';', index=False)
