import pandas as pd
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv('data/combined_osmi_survey_cleaned.csv')

# Print column names to see what's available
print(df.columns)

# Clean column names (remove leading/trailing spaces if needed)
df.columns = df.columns.str.strip()

# Define your features list
features = [
    "Are you self-employed?", "employer_mh_benefits",
    "Do you know the options for mental health care available under your employer-provided coverage?",
    "Has your employer ever formally discussed mental health?",
    "Does your employer offer resources to learn more about mental health concerns and options for seeking help?",
    "Would you feel comfortable discussing a mental health disorder with your coworkers?",
    "Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?",
    "Do you have medical coverage (private insurance or state-provided) which includes treatment of mental health issues?",
    "Do you know local or online resources to seek help for a mental health disorder?",
    "current_mental_disorder", "age", "gender"
]

# Check if all features are in the dataset
missing_features = [feature for feature in features if feature not in df.columns]
if missing_features:
    print(f"The following columns are missing: {missing_features}")
    # You may choose to remove them from the features list
    features = [feature for feature in features if feature not in missing_features]

# Handle missing values
imputer = SimpleImputer(strategy='most_frequent')
df[features] = imputer.fit_transform(df[features])

# Continue with model training or further processing
