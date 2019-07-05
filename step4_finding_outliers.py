import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""""""""
df = pd.read_csv("datasets/preprocessing3.1_genderspecific_clothing/preprocessing_genderspecific_article.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)
numeric_columns = df.loc[:, [[df['ABSATZ'], df['PPRICE'], df['GROESSE'], df['BESTELLSUMME'], df['COUPONWERT'], df['MARKTKENNZEICHEN'], df['CLOTHING_GENDER'], df['CLOTHING_GENDER_UNIQUE']]]]
num_df = pd.DataFrame(numeric_columns)

n_rows = 5
n_cols = 6
count = 0
col_num = 1

plt.subplots(n_rows, n_cols)
for i in range(n_rows):
    for j in range(n_cols):
        plt.subplot(n_rows, n_cols, count+1)
        sns.boxplot(num_df.iloc[:, col_num], orient='vertical')
        if col_num < num_df.shape[1]:
            count += 1
            col_num += 1

plt.show()





#________
df = pd.read_csv("datasets/preprocessing3.1_genderspecific_clothing/preprocessing_genderspecific_article.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)
#numeric_columns = df.loc[:, df.columns != [df['ABSATZ'], df['PPRICE'], df['GROESSE'], df['BESTELLSUMME'], df['COUPONWERT'], df['PROMOTIONNR'], df['MARKTKENNZEICHEN'], df['ARTIKELNR'], df['ANZAHL'], df['ARTIKELNR']]]



boxp = sns.boxplot(x = df['GROESSE'], data = df)
plt.show()


low = .05
high = .95
quant_df = numeric_columns.quantile([low, high])
print(quant_df)


#FUNCTION TO DETECT OUTLIERS
def detect_outliers(column):
    value_list = column.tolist()
    threshold = 3
    mean = np.mean(column)
    std = np.std(column)

    for value in value_list:
        z_score = (value - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(value)

    print(len(outliers))
    return outliers


#CREATING DATASET WITH DETECTED OUTLIERS
outliers = pd.DataFrame(detect_outliers(df['VIEWTIME_IN_S']))

#GETTING IGD
#sorted(df) #nach welcher Spalte wird sortiert? wenn ich eine spalte sortiere, kriege ich das df nie wieder richtig zusammen -> index mitliefern?


#VISUALIZING THE DISTRIBUTION OF NUMERIC COLUMNS
#for column in numeric_columns:
"""""""""
