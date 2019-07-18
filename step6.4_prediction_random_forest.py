# IMPORT BOUNDARIES
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

# LOAD DATA
df = pd.read_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", error_bad_lines=False, sep=';', low_memory=False)

# SPLIT DATA IN TRAIN AND TEST
y = df['ANREDE']
X = df.drop(['ANREDE'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# SCALING DATA
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# NEXT PART IS ONLY TO BE EXECUTED ONCE TO FIND BEST PARAMETERS
'''''''''
# SEARCHING FOR BEST PARAMETERS
grid_params = {'n_estimators': [400, 500, 600],
               'max_features': ['sqrt', 'log2'],
               'max_depth': [200, 225, 250]}

gs = GridSearchCV(RandomForestClassifier(),
                  grid_params,
                  verbose=1,
                  cv=3,
                  n_jobs=-1)

gs_results = gs.fit(X_train, y_train)

print(gs_results.best_score_)
print(gs_results.best_estimator_)
print(gs_results.best_params_)
'''''''''

# CREATE AND FIT MODEL
regressor = RandomForestClassifier(max_depth=225, max_features='sqrt', n_estimators=500)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)

# SHOW ACCURACY
print("Random Forest: ", accuracy_score(y_test, predictions.round(), normalize=True))

# ECHO OUTPUT IN FILE
sys.stdout = open("c:\\Projekt\projekt_geschlecht2\Echo_files\\random_forest.txt", "w")
print("Random Forest got an accuracy score of ", round(accuracy_score(y_test, predictions), 3) * 100, "%.")
