import numpy as np
import pandas as pd
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

# SEARCHING FOR BEST PARAMETERS
grid_params = {'n_estimator': [200, 700],
               'max_features': ['sqrt', 'log2'],
               'max_depth': [8, 9, 10, 11, 12]}

gs = GridSearchCV(RandomForestClassifier(),
                  grid_params,
                  verbose=1,
                  cv=3,
                  n_jobs=-1)

gs_results = gs.fit(X_train, y_train)

print(gs_results.best_score_)
print(gs_results.best_estimator_)
print(gs_results.best_params_)

# FIT MODEL
regressor = RandomForestClassifier(gs_results)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# SHOW ACCURACY
print("Random Forest: ", accuracy_score(y_test, y_pred.round(), normalize=True))
