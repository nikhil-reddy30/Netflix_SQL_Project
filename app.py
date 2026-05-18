import streamlit as st
import pandas as pd

st.title("Netflix SQL Data Analysis Dashboard")

df = pd.read_csv("netflix_titles.csv")

st.subheader("Netflix Dataset Preview")
st.dataframe(df)

st.subheader("Content Type Distribution")
st.bar_chart(df["type"].value_counts())

st.subheader("Top 10 Countries")
country_counts = df["country"].dropna().str.split(", ").explode().value_counts().head(10)
st.bar_chart(country_counts)

st.subheader("Release Year Distribution")
st.line_chart(df["release_year"].value_counts().sort_index())
