# IMPORT BOUNDARIES
import pandas as pd
import sys
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

# LOAD DATA
df = pd.read_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", error_bad_lines=False, sep=';', low_memory=False)

# SPLIT DATA IN TRAIN AND TEST SETS
y = df['ANREDE']
X = df.drop(['ANREDE'], axis=1) #, 'CLOTHING_GENDER_UNIQUE'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# SCALING DATA
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# CREATING THE MODEL, FITTING AND PREDICTING
logmodel = linear_model.LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

# PRINT OF CERTAIN SCORES
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print("Logistic Regression got an accuracy score of ", round(accuracy_score(y_test, predictions), 3)*100, "%.")

# ECHO OUTPUT IN FILE
sys.stdout = open("c:\\Projekt\projekt_geschlecht2\Echo_files\logreg.txt", "w")
print("Logistic Regression got an accuracy score of ", round(accuracy_score(y_test, predictions), 3)*100,"%.")
