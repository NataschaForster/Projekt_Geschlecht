# IMPORT BOUNDARIES
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# LOAD DATA
df = pd.read_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", error_bad_lines=False, sep=';',
                 low_memory=False)

# SPLIT DATA IN TRAIN AND TEST
y = df['ANREDE']
X = df.drop(['ANREDE'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# SCALING DATA
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# FIT MODEL
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(X_train, y_train.values.ravel())

# PREDICTION
predictions = mlp.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
print("Accuracy:", metrics.accuracy_score(y_test, predictions))

# ECHO OUTPUT IN FILE
sys.stdout = open("c:\\Projekt\projekt_geschlecht2\Echo_files\\neural_network.txt", "w")
print("Neural Network got an accuracy score of ", round(metrics.accuracy_score(y_test, predictions), 3) * 100, "%.")
