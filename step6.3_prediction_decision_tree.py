# IMPORT BOUNDARIES
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# LOAD DATA
df = pd.read_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", error_bad_lines=False, sep=';', low_memory=False)

# SPLIT DATA IN TRAIN AND TEST
y = df['ANREDE']
X = df.drop(['ANREDE'], axis=1) #, 'CLOTHING_GENDER_UNIQUE'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# SCALING DATA
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

'''''''''
# SEARCHING FOR BEST PARAMETERS
grid_params = {'min_samples_leaf': range(1, 2),
               'max_depth': range(50, 150, 2)}

gs = GridSearchCV(DecisionTreeClassifier(),
                  grid_params,
                  verbose=1,
                  cv=3,
                  n_jobs=-1)

gs_results = gs.fit(X_train, y_train)

print(gs_results.best_score_)
print(gs_results.best_estimator_)
print(gs_results.best_params_)

'''''''''
# DECISION TREE MODEL AND FITTING TO TRAIN SET
clf_gini = DecisionTreeClassifier(random_state=1, max_depth=88, min_samples_leaf=1)
clf_gini.fit(X_train, y_train)

# PREDICTION
predictions = clf_gini.predict(X_test)

# SHOW ACCURACY
print("Decision Tree: ", accuracy_score(y_test, predictions))

# ECHO OUTPUT IN FILE
sys.stdout = open("c:\\Projekt\projekt_geschlecht2\Echo_files\decision_tree.txt", "w")
print("Decision Tree got an accuracy score of ", round(accuracy_score(y_test, predictions), 3)*100, "%.")
