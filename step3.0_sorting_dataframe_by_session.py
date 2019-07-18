#IMPORT BOUNDARIES
import pandas as pd

# IMPORT DATA
df = pd.read_csv("datasets/preprocessing2_filling_empty_cells/preprocessed_mean.csv", error_bad_lines=False, header=0, sep=';', low_memory=False)

# SORTING AND REPLACING THE DATAFRAME
df.sort_values('SESSION_ID', inplace=True)

# CREATING NEW CSV
df.to_csv("datasets/preprocessing3.0_sorting_session/preprocessing_session_sorted.csv", sep=';', index=False)
