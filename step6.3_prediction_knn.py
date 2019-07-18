import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler


# READ DATA
df = pd.read_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

# Split dataset into training set and test set
y = df['ANREDE']
X = df.drop(['ANREDE'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# SCALING DATA
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

'''''''''
# SEARCHING FOR BEST PARAMETERS
grid_params = {'n_neighbors': [3,5,7,9,11],
               'weights': ['uniform', 'distance'],
               'metric': ['euclidean', 'manhattan']}

gs = GridSearchCV(KNeighborsClassifier(),
                  grid_params,
                  verbose=1,
                  cv=3,
                  n_jobs=-1)

gs_results = gs.fit(X_train, y_train)

print(gs_results.best_score_)
print(gs_results.best_estimator_)
print(gs_results.best_params_) n_neighbors=9, weights='distance', metric='manhattan'
'''''''''

# Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=9, weights='distance', metric='manhattan')

# Train the model using the training sets
knn.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = knn.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Erfolgsrate des kNN Algorithmus: ", round(metrics.accuracy_score(y_test, y_pred),3)*100, "%")

# ECHO OUTPUT IN FILE
sys.stdout = open("c:\\Projekt\projekt_geschlecht2\Echo_files\knn.txt", "w")
print("k-NearestNeighbor got an accuracy score of ", round(metrics.accuracy_score(y_test, y_pred), 3)*100, "%.")
