import streamlit as st
import pandas as pd
from textblob import TextBlob

st.title("💬 Sentiment Analysis on Open-Ended Responses")

# Load cleaned dataset
df = pd.read_csv("combined_osmi_survey.csv")

# Drop elaborative "Why or why not?" columns
df = df.loc[:, ~df.columns.str.lower().str.contains("why or why not")]

# Define a list of high-signal, open-ended columns
sentiment_candidates = [
    col for col in df.columns
    if any(keyword in col.lower() for keyword in [
        "describe", "experience", "reaction", "response",
        "what do you think", "how has", "circumstances",
        "conversation", "please use this space"
    ]) and df[col].dtype == "object"
]

if not sentiment_candidates:
    st.warning("No suitable sentiment analysis columns found.")
else:
    selected_col = st.selectbox("📝 Choose a question for sentiment analysis:", sentiment_candidates)

    df_sentiment = df[[selected_col]].dropna().copy()
    df_sentiment["Sentiment"] = df_sentiment[selected_col].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

    st.write("📈 Sentiment scores (from -1 = Negative to 1 = Positive):")
    st.dataframe(df_sentiment.sort_values("Sentiment", ascending=False))

    st.line_chart(df_sentiment["Sentiment"].sort_values().reset_index(drop=True))

    st.subheader("📊 Sentiment Distribution")
    st.bar_chart(df_sentiment["Sentiment"].round(1).value_counts().sort_index())
