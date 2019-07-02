import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("datasets/preprocessed_mean.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

#LIST OF ALL NUMERIC COLUMNS9
numeric_columns = [df['VIEWTIME_IN_S'], df['ABSATZ'], df['PPRICE'], df['GROESSE'], df['BESTELLSUMME'], df['COUPONWERT'], df['PROMOTIONNR'], df['MARKTKENNZEICHEN'], df['ARTIKELNR'], df['ANZAHL'], df['ARTIKELNR']]