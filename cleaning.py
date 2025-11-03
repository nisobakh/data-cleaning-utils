# Data Cleaning Utilities
# Simple functions for preparing raw data

import pandas as pd
import numpy as np

def remove_duplicates(df):
    """Remove duplicate rows from a DataFrame."""
    return df.drop_duplicates()

def fill_missing(df, columns, value=None):
    """Fill missing values in given columns with a default value or column mean."""
    for col in columns:
        if value is not None:
            df[col] = df[col].fillna(value)
        else:
            df[col] = df[col].fillna(df[col].mean())
    return df

def normalize_column(df, column):
    """Normalize a numeric column between 0 and 1."""
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df

# Example usage
if __name__ == "__main__":
    data = {"age": [25, 30, 25, None], "score": [80, 95, 80, 70]}
    df = pd.DataFrame(data)
    df = remove_duplicates(df)
    df = fill_missing(df, ["age"])
    df = normalize_column(df, "score")
    print(df)
