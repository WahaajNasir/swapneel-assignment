import streamlit as st
import pandas as pd

st.title("📊 Overview of OSMI Mental Health Survey Data")

# Load cleaned data
df = pd.read_csv("D:/Uni/Swapneel 2/data/combined_osmi_survey_cleaned.csv")

# Show top 10 countries
if "country" in df.columns:
    st.subheader("🌍 Top 10 Countries (Survey Respondents)")
    country_counts = df["country"].value_counts().head(10)
    st.bar_chart(country_counts)
else:
    st.warning("No 'country' column found in dataset.")

import altair as alt

# Age distribution
if "age" in df.columns:
    st.subheader("🎂 Age Distribution")

    # Convert age to numeric safely
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df_age_clean = df[(df["age"] >= 10) & (df["age"] <= 100)]

    age_chart = (
        alt.Chart(df_age_clean)
        .mark_bar()
        .encode(
            alt.X("age:Q", bin=alt.Bin(maxbins=30), title="Age"),
            alt.Y("count()", title="Number of Respondents"),
        )
        .properties(width=700, height=400)
    )

    st.altair_chart(age_chart)
else:
    st.warning("No 'age' column found in dataset.")

# Gender
def normalize_gender(g):
    g = str(g).strip().lower()
    if g in ["male", "m", "man", "cis male", "cis man"]:
        return "Male"
    elif g in ["female", "f", "woman", "cis female", "cis woman"]:
        return "Female"
    elif "non-binary" in g or "nonbinary" in g or "genderqueer" in g or "gender fluid" in g:
        return "Non-binary"
    else:
        return "Other"

if "gender" in df.columns:
    st.subheader("⚥ Gender Distribution")

    # Apply normalization
    df["gender_cleaned"] = df["gender"].apply(normalize_gender)

    # Show counts
    gender_counts = df["gender_cleaned"].value_counts()
    st.bar_chart(gender_counts)
else:
    st.warning("No 'gender' column found in dataset.")

# Mental health disorder prevalence
if "current_mental_disorder" in df.columns:
    st.subheader("🧠 Currently Have a Mental Health Disorder?")
    mh_counts = df["current_mental_disorder"].value_counts()
    st.bar_chart(mh_counts)
