"""Practical 9.2 - Streamlit dashboard.

Run locally:  streamlit run 9_2_streamlit_dashboard.py

In Google Colab see the notebook cell for this practical (it needs a tunnel).
"""
import pandas as pd
import streamlit as st

st.title("Student Dashboard")

data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 85],
}
df = pd.DataFrame(data)

st.subheader("Student data")
st.dataframe(df)

st.subheader("Marks")
# Original used st.bar_chart(df['Marks']) which labels bars 0,1,2; index by name.
st.bar_chart(df.set_index("Name")["Marks"])

st.metric("Average marks", f"{df['Marks'].mean():.1f}")
