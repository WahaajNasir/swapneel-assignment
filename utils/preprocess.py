import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.strip()
    if 'gender' in df.columns:
        df['gender'] = df['gender'].fillna("Not specified")
    if 'country' in df.columns:
        df['country'] = df['country'].fillna("Not specified")
    return df