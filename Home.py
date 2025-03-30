import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Mental Health in Tech Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Mental Health in Tech Dashboard")
st.markdown("""
Welcome to the interactive dashboard analyzing the OSMI Mental Health in Tech Survey data from 2016 to 2020.

Use the sidebar to navigate between pages:

- 📊 **Overview**: General trends and insights
- 💬 **Sentiment Analysis**: Word clouds and text sentiment from open-ended responses
- 🧠 **Predictions**: Predict likelihood of mental health disorder using survey features
- 📈 **Trends**: Explore workplace support, awareness, and stigma across years
- 📂 **Sample Data**: View and filter raw survey data

Make sure your `data/` folder contains the 5 survey CSVs.
""")

# Check for data files
data_path = Path("data")
csv_files = list(data_path.glob("*.csv"))
if not csv_files:
    st.error("⚠️ No CSV files found in the data/ folder. Please add the survey datasets.")
else:
    st.success(f"✅ {len(csv_files)} datasets found in the data/ folder.")
