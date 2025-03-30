import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
from sklearn.impute import SimpleImputer


def train_and_save_model(df):
    # Define the features and target
    features = [
        "Are you self-employed?", "employer_mh_benefits",
        "Do you know the options for mental health care available under your employer-provided coverage?",
        "Has your employer ever formally discussed mental health?",
        "Does your employer offer resources to learn more about mental health concerns and options for seeking help?",
        "Would you feel comfortable discussing a mental health disorder with your coworkers?",
        "Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?",
        "Do you think that discussing a mental health disorder with your employer would have negative consequences?",
        "Have you had a mental health disorder in the past?",
        "current_mental_disorder", "sought_treatment",
        "Do you have medical coverage (private insurance or state-provided) which includes treatment of mental health issues?",
        "Do you believe your productivity is ever affected by a mental health issue?",
        "age", "gender",
        "Do you know local or online resources to seek help for a mental health disorder?"
    ]
    target = "current_mental_disorder"

    # Check for missing columns in the dataset and adjust the feature list
    missing_columns = []
    for col in features:
        if col not in df.columns:
            missing_columns.append(col)
            features.remove(col)

    # Print out the missing columns that were removed
    if missing_columns:
        print(f"Removed the following missing columns from features: {', '.join(missing_columns)}")

    # Impute missing values with the most frequent value (for categorical) or the mean (for numerical)
    imputer = SimpleImputer(
        strategy='most_frequent')  # Use 'mean' for numerical columns, 'most_frequent' for categorical
    df[features] = imputer.fit_transform(df[features])

    # Clean and preprocess the data (ensure target column is non-null)
    df_clean = df.dropna(subset=[target])

    # Check if the cleaned dataset is empty
    if df_clean.empty:
        print("Warning: The dataset is empty after dropping rows with missing target values.")
        return None, None, None

    # Encode categorical variables
    le = LabelEncoder()
    for col in features:
        if df_clean[col].dtype == 'object':
            df_clean[col] = le.fit_transform(df_clean[col].astype(str))

    # Split the dataset into features and target
    X = df_clean[features]
    y = df_clean[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, 'mental_health_model.pkl')

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Print model evaluation metrics
    print(f"Model Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(report)

    return model, accuracy, report


# Example of how to call the function from another script
if __name__ == "__main__":
    # Load your dataset
    df = pd.read_csv('data/combined_osmi_survey_cleaned.csv')  # Adjust the path to your actual dataset location

    # Call the function to train the model
    model, accuracy, report = train_and_save_model(df)

    if model is not None:
        print("Model trained and saved successfully!")
    else:
        print("Model training failed due to empty dataset.")
