import pandas as pd
import os

DATA_FOLDER = "data"

def load_all_surveys():
    dfs = []
    for year in range(2016, 2021):
        path = os.path.join(DATA_FOLDER, f"OSMI Mental Health in Tech Survey {year}.csv")
        try:
            df = pd.read_csv(path)
            df["survey_year"] = year
            dfs.append(df)
        except FileNotFoundError:
            continue
    return pd.concat(dfs, ignore_index=True)