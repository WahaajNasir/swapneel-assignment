import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Visualizations")
st.markdown("Explore key trends from the OSMI Mental Health in Tech Survey (2016-2020).")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/combined_osmi.csv")
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("No data available.")
    st.stop()

# Year selection
years = df['Year'].dropna().unique()
selected_year = st.selectbox("Select Year", sorted(years))

# Filter data
df_year = df[df["Year"] == selected_year]

# Attempt to find a coworker-related column
coworker_cols = [col for col in df.columns if "coworker" in col.lower() and df[col].notna().sum() > 0]

if not coworker_cols:
    st.warning("Coworker-related data not found for this year.")
else:
    selected_col = st.selectbox("Select a coworker-related question", coworker_cols)
    value_counts = df_year[selected_col].value_counts(dropna=False)

    if value_counts.empty:
        st.warning("No responses for this question in the selected year.")
    else:
        st.subheader(f"Responses for: {selected_col}")
        vc_df = value_counts.reset_index()
        vc_df.columns = ["Response", "Count"]

        fig = px.bar(vc_df, x="Response", y="Count",
                     labels={"Response": "Response", "Count": "Count"},
                     title=f"Distribution of Responses ({selected_year})")
        st.plotly_chart(fig, use_container_width=True)
