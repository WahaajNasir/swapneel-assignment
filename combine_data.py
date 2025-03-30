# combine_data.py

import pandas as pd
import os

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.replace('\u00a0', ' ') \
        .str.replace('Â', '').str.replace(r'\s+', ' ', regex=True)
    return df

def load_and_combine_data(data_dir='data'):
    combined_df = pd.DataFrame()

    for year in range(2016, 2021):
        file_name = f"OSMI Mental Health in Tech Survey {year}.csv"
        file_path = os.path.join(data_dir, file_name)

        try:
            df = pd.read_csv(file_path)
            df = clean_column_names(df)
            df['Year'] = year
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            print(f"Error loading {file_name}: {e}")

    # Save combined file
    combined_csv_path = os.path.join(data_dir, 'combined_osmi.csv')
    combined_df.to_csv(combined_csv_path, index=False)
    print(f"✅ Combined CSV saved to {combined_csv_path}")

    return combined_df

if __name__ == "__main__":
    load_and_combine_data()
