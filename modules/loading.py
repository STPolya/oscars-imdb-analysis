import pandas as pd

def load_files(file_path, separator, usecols = None):
    return pd.read_csv(file_path, sep=separator, na_values=[r'\N'], usecols=usecols)