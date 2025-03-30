import pandas as pd
import os
from glob import glob

# Path to all survey CSV files
data_dir = 'D:/Uni/Swapneel 2/data'
csv_files = glob(os.path.join(data_dir, 'OSMI Mental Health in Tech Survey *.csv'))

# Define standard column mappings (expand this as needed)
column_map = {
    "What country do you live in?": "country",
    "What is your age?": "age",
    "What is your gender?": "gender",
    "Do you currently have a mental health disorder?": "current_mental_disorder",
    "Have you been diagnosed with a mental health condition by a medical professional?": "diagnosed_disorder",
    "Have you ever sought treatment for a mental health issue from a mental health professional?": "sought_treatment",
    "Do you have a family history of mental illness?": "family_history",
    "Does your employer provide mental health benefits as part of healthcare coverage?": "employer_mh_benefits",
    "Do you feel that your employer takes mental health as seriously as physical health?": "employer_mh_serious",
    "What country do you work in?": "work_country",
    "What US state or territory do you live in?": "us_state_live",
    "What US state or territory do you work in?": "us_state_work",
}

normalized_dataframes = []

for file_path in csv_files:
    year = os.path.basename(file_path).split()[-1].split('.')[0]
    print(f"🔄 Normalizing columns for year {year}...")

    df = pd.read_csv(file_path, low_memory=False)

    # Clean column names
    df.columns = df.columns.str.strip().str.replace('"', '').str.replace('\n', ' ').str.replace('\r', '')

    # Rename columns based on mapping
    df = df.rename(columns={col: column_map[col] for col in df.columns if col in column_map})

    # Add year column
    df["year"] = int(year)

    normalized_dataframes.append(df)

print("\n📊 Combining all datasets into one unified DataFrame...")
combined_df = pd.concat(normalized_dataframes, ignore_index=True)

# Save to cleaned CSV
cleaned_path = os.path.join(data_dir, 'combined_osmi_survey_cleaned.csv')
combined_df.to_csv(cleaned_path, index=False)
print(f"✅ Saved cleaned dataset to '{cleaned_path}'")
