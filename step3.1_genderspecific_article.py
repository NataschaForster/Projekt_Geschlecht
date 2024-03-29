# IMPORT BOUNDARIES
import pandas as pd

# LOAD DATA
df = pd.read_csv("datasets/preprocessing3.0_sorting_session/preprocessing_session_sorted.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)


# NEW COLUMN WITH "WATCHED WOMENS/MENS CLOTHING" BY SEARCHING IN URL STRING
def gender_article(s):
    content_list = s.to_list()
    word_list_damen = ["Damen", "damen" "BHs", "Kleider", "Blusen", "Mieder"]
    word_list_herren = ["Herren", "herren", "Pollunder", "Boxershorts"]
    new_column_list = []
    counter = 0
    counter_herren = 0

    # COMPARE URL CONTENT WITH WORD LIST
    for line in content_list:
        for word in word_list_damen:
            if str(word) in str(line):
                counter = counter + 1
        for word in word_list_herren:
            if str(word) in str(line):
                counter_herren += 1

        # APPEND MATCHING NUMBER TO NEW LIST
        if counter_herren > 0:
            new_column_list.append(0)#masculine clothing
        elif counter > 0:
            new_column_list.append(1) #feminine clothing
        else:
            new_column_list.append(2) #no gendered clothing

        counter = 0
        counter_herren = 0

    return pd.Series(new_column_list)


# NEW COLUMN WITH "WATCHED WOMENS/MENS CLOTHING" BY SEARCHING IN URL STRING
def search_gender(s):
    content_list = s.to_list()
    search_damen = ["Damen", "damen", "BHs", "Kleider", "Blusen", "blusen", "BH", "frau", "Frau", "Nachthemd",
                    "nachthemd", "Slip", "Mieder", "mieder", "slip", "Tunika", "tunika", "Blazer", "blazer" "Leggings",
                    "leggings", "Leggins", "leggins", "Schlüpfer", "schlüpfer", "Tasche", "tasche", "bh"]
    search_herren = ["Herren", "herren", "Pollunder", "Boxershorts", "Männer", "männer", "Mann", "mann"]
    new_column_list = []
    counter = 0
    counter_herren = 0

    # COMPARE URL CONTENT WITH WORD LIST
    for line in content_list:
        for word in search_damen:
            if str(word) in str(line):
                counter = counter + 1
        for word in search_herren:
            if str(word) in str(line):
                counter_herren += 1

        # APPEND MATCHING NUMBER TO NEW LIST
        if counter_herren > 0:
            new_column_list.append(0)#masculine clothing
        elif counter > 0:
            new_column_list.append(1) #feminine clothing
        else:
            new_column_list.append(2) #no gendered clothing

        counter = 0
        counter_herren = 0

    return pd.Series(new_column_list)


# FILLING THE DATAFRAME AND CREATING A NEW CSV
df['CLOTHING_GENDER'] = gender_article(df['CONTENT_NAME'].astype(str))
df['SEARCH_GENDER'] = search_gender(df['SEARCH_QUERY'].astype(str))
print("checked for gender clothing")
df.to_csv("datasets/preprocessing3.1_genderspecific_clothing/preprocessing_genderspecific_article.csv", sep=';', index=False)

