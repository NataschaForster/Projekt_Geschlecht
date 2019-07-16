import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
from sklearn import svm
from matplotlib import style
style.use("ggplot")


# LOAD DATA
df = pd.read_csv("datasets/preprocessing5_balance_gender/balanced_gender.csv", error_bad_lines=False, sep=';', low_memory=False)
y = df['ANREDE']
X = df.drop(['ANREDE'], axis=1)

# CREATING THE MODEL
model = SVC(kernel='linear', C=1E10)
model.fit(X, y)

